from django.db import models

class Face_img(models.Model):
    fileName = models.CharField(max_length=255, default='')
    realAge = models.CharField(max_length=10)
    faceImg = models.ImageField(upload_to="face_img")

    def __str__(self):
        return self.fileName
    
class Predict_age(models.Model):
    realAge = models.IntegerField()
    predictAge = models.IntegerField()
