from django.db import models

class Face_img(models.Model):
    realAge = models.IntegerField()
    faceImg = models.ImageField(upload_to="face_img")

    def __str__(self):
        return self.fileName
    
class Predict_age(models.Model):
    realAge = models.IntegerField()
    predictAge = models.IntegerField()
    diff = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default='m')
