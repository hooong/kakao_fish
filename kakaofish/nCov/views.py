from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from selenium import webdriver

import requests
from .models import *
# from tag.models import Tag
import re
def coIndex(request):
    # driver = webdriver.Firefox()
    # driver.get("https://thewuhanvirus.com/")
    
    # html = driver.page_source
    # soup = BeautifulSoup(html)

    # p_table = soup.find("table", {"class":"table table-bordered"})
    # print(p_table)

    # 뉴스 크롤링
    # 스케줄러로 돌리고 db에 저장하고 db에서 상위 몇개씩 가져오면 된다.
    url = "https://openapi.naver.com/v1/search/news.json"
    query = "코로나"

    request_url = url + '?query=' + query + '&display=15'
    Client_Id = "sIROnlLXckZke3JED_1d"
    Client_Secret = "LeMrSZcrCx"
    headers = {'X-Naver-Client-Id': Client_Id, "X-Naver-Client-Secret": Client_Secret}

    response_url = requests.get(request_url, headers=headers)
    news = response_url.json()
    n=len(news['items'])
    for i in range(len(news['items'])):
        for key,value in news['items'][i].items():
            news['items'][i][key]=news['items'][i][key].replace("<b>","")
            news['items'][i][key]=news['items'][i][key].replace("</b>","")
            news['items'][i][key]=news['items'][i][key].replace("&quot;","")
            # print(news['items'][i][key])
    news = News.objects.all().order_by('-id')[:10]
    # print(news)
    context = {'news':news}
    boards = Board.objects.order_by('-id')
    return render(request, 'index.html', {'context':context,'boards':boards})



def board_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    if request.method == "GET":
        form = BoardForm()

    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_board = Board(
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer = user
            )
            new_board.save()

            ### 태그 추가 부분 ###
            tags = form.cleaned_data['tag'].split(',')
            for tag in tags:
                if not tag : 
                    continue
                else:
                    tag = tag.strip()
                    tag_, created = Tag.objects.get_or_create(name = tag)
                    new_board.tag.add(tag_)

            return redirect('/board/list')

    return render(request, 'board_write.html', {'form' :form})
