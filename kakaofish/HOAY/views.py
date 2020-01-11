from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from bs4 import BeautifulSoup as bs
import requests, os, json

# 사진이랑 나이 입력화면
def hoaymain(request):
    if request.method == 'POST':
        faceimgform = FaceImgForm(request.POST, request.FILES)
        filename = request.FILES['faceImg']
        if faceimgform.is_valid():
            face_img = faceimgform.save(commit=False)
            face_img.fileName = filename
            face_img.save()
            img_id = face_img.id

        return redirect('/hoay/predict/' + str(img_id))
    else:
        faceForm = FaceImgForm()
        context = {'faceForm': faceForm}

        return render(request, "hoyamain.html", context)

# 결과보여주는 화면
def result(request, id):
    pre = Predict_age.objects.get(id=id)
    gender = pre.gender
    realage = pre.realAge
    age = pre.predictAge

    if gender == 'm':
        gender = '남자'
    else:
        gender = '여자'

    age_distance = int(realage) - int(age)
    age_dis = abs(age_distance)
    
    # 동안 or 노안
    if age_distance < 0:
        young_or_older = 'older'
    elif age_distance > 0:
        young_or_older = 'younger'
    else:
        young_or_older = 'same'

    # 순위 시스템
    


    context = {'gender': gender, 'age': age, 'young_or_older': young_or_older, 'age_dis': age_dis}
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

    faceInfo_all = result.json()
    print(faceInfo_all)
    if len(list(faceInfo_all['result'])) == 2:
        return redirect('error')
    faceInfo = faceInfo_all['result']['faces'][0]['facial_attributes']
    gender = faceInfo['gender']
    m = float(gender['male'])
    f = float(gender['female'])
    if m > f:
        gender = 'm'
    else:
        gender = 'f'

    age = faceInfo['age']
    age = str(round(float(age)))

    tmp_predict = Predict_age()
    tmp_predict.predictAge = age
    tmp_predict.realAge = realAge 
    tmp_predict.diff = abs(int(realAge)-int(age))
    tmp_predict.gender = gender
    tmp_predict.save()
    pre_id = tmp_predict.id

    return redirect('/hoay/result/' + str(pre_id))