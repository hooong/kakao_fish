from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from django.conf import settings
from bs4 import BeautifulSoup as bs
from django.http import JsonResponse
import requests, os, json, random, base64

# 사진이랑 나이 입력화면
def index(request):
    return render(request, "index.html")
    
def hoaymain(request):
    if request.method == 'POST':
        faceimgform = FaceImgForm(request.POST, request.FILES)
        filename = request.FILES['faceImg']
        if faceimgform.is_valid():
            face_img = faceimgform.save(commit=False)
            face_img.save()
            img_id = face_img.id

        return redirect('/hoay/predict/' + str(img_id))
    else:
        faceForm = FaceImgForm()
        context = {'faceForm': faceForm}

        return render(request, "hoyamain.html", context)

# 결과보여주는 화면
def result(request, id):
    if 'fbclid' in request.GET:
        return redirect('hoaymain')
    else:
        pre = Predict_age.objects.get(id=id)
        gender = pre.gender
        realage = pre.realAge
        age = pre.predictAge
        diff = pre.diff

        if gender == 'm':
            gender = '남자'
        elif gender == 'f':
            gender = '여자'
        else:
            gender = '자웅동체'
        
        # 동안 or 노안
        if diff > 0:
            young_or_older = 'older'
        elif diff < 0:
            young_or_older = 'younger'
        else:
            young_or_older = 'same'

        # 순위 시스템
        tier, percent = tierSystem(diff)

        context = {'gender': gender, 'age': age, 
                    'young_or_older': young_or_older, 'age_dis': abs(diff),
                    'tier': tier, 'percent': percent, 'id':id}
        return render(request, "result.html", context)

def error(request):
    return render(request, 'error.html')

# 나이예측
def predictAge(request, id):
    CONFIG_SECRET_DIR = os.path.join(settings.ROOT_DIR, '.config_secret')
    CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
    config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

    faceImg = Face_img.objects.get(id=id)
    faceImgfile = os.path.join(settings.BASE_DIR, 'media/'+str(faceImg.faceImg))
    realAge = faceImg.realAge

    API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
    APP_KEY = config_secret_common['django']['kakaokey']
    headers = {'Authorization': 'KakaoAK {}'.format(APP_KEY)}
    file = { 'file' : open(faceImgfile, 'rb')}

    result = requests.post(API_URL, headers=headers, files=file)

    os.remove(faceImgfile)
    faceImg.delete()

    if result.status_code != 200:
        return redirect('error')

    faceInfo_all = result.json()
    if len(list(faceInfo_all['result'])) == 2:
        return redirect('error')
    faceInfo = faceInfo_all['result']['faces'][0]['facial_attributes']
    gender = faceInfo['gender']
    m = float(gender['male'])
    f = float(gender['female'])
    if abs(m - f) < 0.1:
        gender = 'h' 
    else:
        if m > f:
            gender = 'm'
        else:
            gender = 'f'

    age = faceInfo['age']
    age = str(round(float(age)))

    tmp_predict = Predict_age()
    tmp_predict.predictAge = age
    tmp_predict.realAge = realAge
    tmp_predict.diff = int(age) - int(realAge)
    tmp_predict.gender = gender
    tmp_predict.save()
    pre_id = tmp_predict.id

    return redirect('/hoay/result/' + str(pre_id))

# 계급 시스템
def tierSystem(diff):

    allCount = Predict_age.objects.count()
    print(allCount)
    diffCount = Predict_age.objects.filter(diff__lte=diff).count()
    print(diffCount)

    percent = int((diffCount / allCount) * 100)
    print(percent)

    if percent < 5:
        tier = 'Master'
    elif percent < 15:
        tier = 'Diamond'
    elif percent < 30:
        tier = 'Platinum'
    elif percent < 50:
        tier = 'Gold'
    elif percent < 80:
        tier = 'Silver'
    elif percent < 95:
        tier = 'Bronze'
    else:
        tier = 'Iron'

    return tier, percent

# canvas 이미지 저장
@csrf_exempt
def canvasToImage(request):
    number = request.POST['data[num]']
    data = request.POST['data[image]']
    data = data[22:]
    
    path = str(os.path.join(settings.STATIC_ROOT, 'resultImg/'))
    filename = 'image' + str(number) + '.png'

    image = open(path+filename, "wb")
    image.write(base64.b64decode(data))
    image.close()

    answer = {'filename': filename}
    return JsonResponse(answer)
