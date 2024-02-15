
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


n_html = requests.get('https://www.irna.ir/rss/tp/20')
n_soup = BeautifulSoup(n_html.content, 'html.parser')
n_heading = n_soup.find_all('title')
n_news = []
for n_header in n_heading:
    n_news.append(n_header.get_text())


v_html = requests.get('https://www.isna.ir/rss/tp/34')
v_soup = BeautifulSoup(v_html.content, 'html.parser')
v_heading = v_soup.find_all('title')
v_news = []
for v_header in v_heading[0:10]:
    v_news.append(v_header.get_text())

def index(request):
    return render(request, 'index.html', {'n_news':n_news, 'v_news':v_news})