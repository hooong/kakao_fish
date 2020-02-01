from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def coIndex(request):
    # driver = webdriver.Firefox()
    # driver.get("https://thewuhanvirus.com/")
    
    # html = driver.page_source
    # soup = BeautifulSoup(html)

    # p_table = soup.find("table", {"class":"table table-bordered"})
    # print(p_table)

    context = {}

    return render(request, 'index.html', context)