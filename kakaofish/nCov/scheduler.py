from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
import requests

# 스케쥴러 생성
def schedule():
    sched = BackgroundScheduler()
    sched.add_job(crawling_news, 'cron', minute='0,30')
    sched.start()

def crawling_news():
    url = "https://openapi.naver.com/v1/search/news.json"
    query = "우한폐렴"

    request_url = url + '?query=' + query + '&display=10'
    Client_Id = "sIROnlLXckZke3JED_1d"
    Client_Secret = "LeMrSZcrCx"
    headers = {'X-Naver-Client-Id': Client_Id, "X-Naver-Client-Secret": Client_Secret}

    response_url = requests.get(request_url, headers=headers)
    news = response_url.json()

    news = news['items']
    for new in news:
        save_new = News()
        save_new.title = new['title']
        save_new.link = new['link']
        save_new.description = new['description']
        save_new.pubDate = new['pubDate']
        save_new.save()
    
    print("sucess news cralwing!")