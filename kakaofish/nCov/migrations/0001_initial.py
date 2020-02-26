# Generated by Django 3.0 on 2020-02-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('pubDate', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='태그명')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그',
                'db_table': 'community_tag',
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('link', models.CharField(max_length=300, verbose_name='링크')),
                ('contents', models.CharField(max_length=30, verbose_name='팩트체크')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
                ('thumbImg', models.ImageField(upload_to='thumb_Img')),
                ('color', models.CharField(choices=[('R', 'RED'), ('B', 'BLUE')], max_length=128)),
                ('tag', models.ManyToManyField(to='nCov.Tag')),
            ],
            options={
                'verbose_name': '게시물',
                'verbose_name_plural': '게시물',
                'db_table': 'community_board',
            },
        ),
    ]
