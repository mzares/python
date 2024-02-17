from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from datetime import datetime
def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.irna.ir/rss/tp/20"
      
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('item')
    for artcile in News[0:10]:
            link = artcile.find('guid').text
            image_src = str(artcile.find('enclosure')['url'])
            title = artcile.find('title').text
            desc = artcile.find('description').text
            # date= datetime.strptime(artcile.find('pubdate').text, " %a , %d %b %Y %H:%M:%S [TZ]")
            # date=artcile.find('pubdate').string
            new_headline = Headline()
            new_headline.desc= desc
            #  new_headline.date= date
            new_headline.title = title
            new_headline.url = link
            new_headline.image = image_src
            new_headline.save()
    return redirect("../")
    
        
def news_list(request):
    headlines = Headline.objects.all()
    context = {
        'object_list': headlines,
    }
    print(context)
    return render(request, "index.html", context)


# n_html = requests.get('https://www.irna.ir/rss/tp/20')
# n_soup = BeautifulSoup(n_html.content, 'html.parser')
# n_heading = n_soup.find_all('item')
# n_news = []
# for artcile in n_heading:
#     # n_news.append(n_header.get_text())
#     title = artcile.find_all('title').
#     link = artcile.find_all('link')
#     image_src = str(artcile.find('enclosure')['url']).split(" ")
#     desc = artcile.find_all('description')
#     new_headline = Headline()
#     new_headline.title = title 
#     new_headline.url = link
#     new_headline.image = image_src
#     new_headline.desc=desc
#     new_headline.save()


# print(new_headline)
# def Web_connect(URL):
#     try:
#         r=requests.get(URL,timeout=10)
#         if r.status_code==200:
#             return r.content
#     except Exception as e:
#         print(repr(e))
# web_url="https://www.isna.ir/rss"
# #print(Web_connect(web_url))
# def Pars_content(content):
#     soup=BeautifulSoup(markup=content, features='xml')
#     articles=soup.find_all('item')
#     news=[]
#     for i in articles:
#         try:
#             title=i.find('title').text
#             link=i.find('link').text
#             desc=i.find('description').text
#             date=i.find('pubDate').text
#             category=i.find('category').text
#             enclosure=i.find('enclosure')
#             article={
#             'title':title,
#             'link':link,
#             'desc':desc,
#             'date':date,
#             'category':category,
#             'enclosure':enclosure
#             }
#             news.append(article)
#         except Exception as e:
#             print(repr(e))
#     return news
# news=Pars_content(Web_connect(web_url))
# print("it is a fild",news[0]) 

# # def map_to_html(article):
# #     return f'''
# #     <div class="col-md-4">
# #         <a href="{article['link']}">
# #             <div class="post-content">
# #                 <figure>
# #                     <img src="#">
# #                     <figcaption class="hover-fig">
# #                         <i class="fa fa-plus"></i>
# #                     </figcaption>
# #                     <figcaption class="date-fig">
# #                         <span>{article['date']}</span>
# #                         <i class="fa fa-date"></i>
# #                     </figcaption>
# #                 </figure>
# #                 <h4>{article['title']}</h4>
# #                 <p>{article['desc']}</p>
# #             </div>
# #         </a>
# #     </div>)
# #     '''
# # Render the HTML content in your template
# # def news_list(request):
# #     headlines = Headline.objects.all()[::-1]
# #     context = {
# #         'object_list': headlines,
# #     }
# #     return render(request, "index.html", context)
# def index(request):
#     html_content = map(map_to_html, news)
#     return render(request, 'index.html', {'n_news':n_news, 'html_content':html_content})
#ok code-----------------------------
# from django.shortcuts import render
# import requests
# from bs4 import BeautifulSoup


# n_html = requests.get('https://www.irna.ir/rss/tp/20')
# n_soup = BeautifulSoup(n_html.content, 'html.parser')
# n_heading = n_soup.find_all('title')
# n_news = []
# for n_header in n_heading:
#     n_news.append(n_header.get_text())


# v_html = requests.get('https://www.isna.ir/rss/tp/34')
# v_soup = BeautifulSoup(v_html.content, 'html.parser')
# v_heading = v_soup.find_all('title')
# v_news = []
# for v_header in v_heading[0:10]:
#     v_news.append(v_header.get_text())

# def Web_connect(URL):
#     try:
#         r=requests.get(URL,timeout=10)
#         if r.status_code==200:
#             return r.content
#     except Exception as e:
#         print(repr(e))
# web_url="https://www.isna.ir/rss"
# # print(Web_connect(web_url))
# def Pars_content(content):
#     soup=BeautifulSoup(markup=content, features='xml')
#     articles=soup.find_all('item')
#     news=[]
#     for i in articles:
#         try:
#             title=i.find('title').text
#             link=i.find('link').text
#             desc=i.find('description').text
#             date=i.find('pubDate').text
#             category=i.find('category').text
#             # enclosure=i.find('enclosure')
#             article={
#             'title':title,
#             'link':link,
#             'desc':desc,
#             'date':date,
#             'category':category,
#             # 'enclosure':enclosure
#             }
#             news.append(article)
#         except Exception as e:
#             print(repr(e))
#     return news
# news=Pars_content(Web_connect(web_url))

# print('it is articel',news[0] )

# def index(request):
#     return render(request, 'index.html', {'n_news':n_news, 'v_news':v_news,'news':news})