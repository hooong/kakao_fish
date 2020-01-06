from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from bs4 import BeautifulSoup as bs
import requests, os

# 사진이랑 나이 입력화면
def hoaymain(request):
    if request.method == 'POST':
        faceimgform = FaceImgForm(request.POST, request.FILES)
        filename = request.FILES['faceImg']
        if faceimgform.is_valid():
            face_img = faceimgform.save(commit=False)
            face_img.fileName = filename
            face_img.save()

        return redirect('/hoay/predict/' + str(filename))
    else:
        faceForm = FaceImgForm()
        context = {'faceForm': faceForm}

        return render(request, "hoyamain.html", context)

# 결과보여주는 화면
def result(request, gender, age, realage):

    if gender == 'm':
        gender = '남자'
    else:
        gender = '여자'

    age_distance = int(realage) - int(age)
    age_dis = abs(age_distance)

    if age_distance < 0:
        young_or_older = 'older'
    elif age_distance > 0:
        young_or_older = 'younger'
    else:
        young_or_older = 'same'

    context = {'gender': gender, 'age': age, 'young_or_older': young_or_older, 'age_dis': age_dis}
    return render(request, "result.html", context)

# 나이예측
def predictAge(request, filename):
    faceImg = Face_img.objects.get(fileName=filename)
    faceImgfile = os.path.join(settings.BASE_DIR, 'media/'+str(faceImg.faceImg))
    realAge = faceImg.realAge

    API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
    APP_KEY = "4225e55822643a967aae27240473a7e6"
    headers = {'Authorization': 'KakaoAK {}'.format(APP_KEY)}
    file = { 'file' : open(faceImgfile, 'rb')}

    result = requests.post(API_URL, headers=headers, files=file)
    result.raise_for_status()

    os.remove(faceImgfile)
    faceImg.delete()

    faceInfo_all = result.json()
    faceInfo = faceInfo_all['result']['faces'][0]['facial_attributes']
    gender = faceInfo['gender']
    m = float(gender['male'])
    f = float(gender['female'])
    if m > f:
        gender = 'm'
    else:
        gender = 'f'
    print(gender)

    age = faceInfo['age']
    age = str(round(float(age)))
    print(age)

    tmp_predict = Predict_age()
    tmp_predict.predictAge = age
    tmp_predict.realAge = realAge 
    tmp_predict.save()

    return redirect('/hoay/result/' + str(gender) + '/' + str(age) + '/' + str(realAge))