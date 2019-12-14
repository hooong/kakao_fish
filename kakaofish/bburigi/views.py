from django.shortcuts import render
from django.conf import settings
import os, json

def bburigi(request):
    CONFIG_SECRET_DIR = os.path.join(settings.ROOT_DIR, '.config_secret')
    CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
    config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

    key = config_secret_common['django']['kakaokey']
    context = {'key':key}
    return render(request, "bburigi.html", context)

def kakiopay(request):
    context = {}
    return render(request, "kakiopay.html", context)
