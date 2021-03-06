"""kakaofish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import bburigi.views
import xmas.views
import HOAY.views
import nCov.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bburigi/', bburigi.views.bburigi, name='bburigi_index'),
    path('', nCov.views.coIndex ,name='index'),
    path('kakiopay/', bburigi.views.kakiopay, name='kakiopay'),
    path('xmas/', xmas.views.xmas, name='xmas'),
    path('hoay/', include('HOAY.urls')),
    path('n_corona/', include('nCov.urls')),
    path('lotto/', include('lotto.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
