from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    pubDate = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "community_tag"
        verbose_name = "태그"
        verbose_name_plural = "태그"


class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    link = models.CharField(max_length=300, verbose_name="링크")
    contents = models.CharField(max_length=30, verbose_name="팩트체크")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    thumbImg = models.ImageField(upload_to="thumb_Img")
    ### 태그 추가 부분 ###
    tag = models.ManyToManyField(Tag, verbose_name = "태그")
    COLOR_CHOICE = (
    ('R', 'RED'),
    ('B', 'BLUE')
    )
    color = models.CharField(choices=COLOR_CHOICE, max_length=128)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "community_board"
        verbose_name = "게시물"
        verbose_name_plural = "게시물"


