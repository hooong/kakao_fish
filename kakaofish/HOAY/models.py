from django.db import models

class face_img(models.Model):
    idNum = models.IntegerField()
    faceImg = models.ImageField(upload_to="face_img")
    
class predict_age(models.Model):
    realAge = models.IntegerField()
    predictAge = models.IntegerField()
