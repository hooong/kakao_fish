from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
import requests

# 스케쥴러 생성
def schedule():
    sched = BackgroundScheduler()
    sched.add_job(crawling_news, 'cron', minute='0,30,15')
    sched.start()

def crawling_news():
    url = "https://openapi.naver.com/v1/search/news.json"
    query = "코로나 미담"

    request_url = url + '?query=' + query + '&display=10'
    Client_Id = "sIROnlLXckZke3JED_1d"
    Client_Secret = "LeMrSZcrCx"
    headers = {'X-Naver-Client-Id': Client_Id, "X-Naver-Client-Secret": Client_Secret}

    response_url = requests.get(request_url, headers=headers)
    news = response_url.json()
    n=len(news['items'])
    for i in range(n):
            for key,value in news['items'][i].items():
                    news['items'][i][key]=news['items'][i][key].replace("<b>","")
                    news['items'][i][key]=news['items'][i][key].replace("</b>","")
                    news['items'][i][key]=news['items'][i][key].replace("&quot;","")
                    print(news['items'][i][key])
    news = news['items']
    for new in news:
        save_new = News()
        save_new.title = new['title']
        save_new.link = new['link']
        save_new.description = new['description']
        # date 설정
        save_new.pubDate = new['pubDate'][:22] 
        save_new.save()
    
    print("sucess news cralwing!")