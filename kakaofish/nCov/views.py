from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from .models import *

def coIndex(request):
    # driver = webdriver.Firefox()
    # driver.get("https://thewuhanvirus.com/")
    
    # html = driver.page_source
    # soup = BeautifulSoup(html)

    # p_table = soup.find("table", {"class":"table table-bordered"})
    # print(p_table)

    # 뉴스 크롤링
    # 스케줄러로 돌리고 db에 저장하고 db에서 상위 몇개씩 가져오면 된다.
    # url = "https://openapi.naver.com/v1/search/news.json"
    # query = "우한폐렴"

    # request_url = url + '?query=' + query + '&display=15'
    # Client_Id = "sIROnlLXckZke3JED_1d"
    # Client_Secret = "LeMrSZcrCx"
    # headers = {'X-Naver-Client-Id': Client_Id, "X-Naver-Client-Secret": Client_Secret}

    # response_url = requests.get(request_url, headers=headers)
    # news = response_url.json()

    news = News.objects.all()

    context = {'news':news}

    return render(request, 'index.html', context)