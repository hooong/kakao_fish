from django import forms
from .models import *

class FaceImgForm(forms.ModelForm):
    class Meta:
        model = Face_img
        fields = ['realAge','faceImg']

        labels = {
            'realAge': '나이',
            'faceImg': '얼굴'
        }