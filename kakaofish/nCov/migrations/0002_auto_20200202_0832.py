# Generated by Django 2.2.2 on 2020-02-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nCov', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pubDate',
            field=models.DateTimeField(),
        ),
    ]