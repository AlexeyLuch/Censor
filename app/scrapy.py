from app import app,db
from models import War
from bs4 import BeautifulSoup
import requests as req
import requests


def parse_all_news_from_war_links(link):
    req = requests.get(link)
    print(link)
    soup = BeautifulSoup(req.content, 'html.parser')
    title = (soup.find(class_='entry-title')).get_text()
    # VIDEo
    summary_img = soup.find(class_='summary_img')
    link_on_img = "default"
    article_description = soup.h2.string
    summary_img = soup.find(class_='entry-content _ga1_on_')
    index = 0
    all_article = ''
    for table in summary_img.findAll('p'):
        if index == 3:
            index = 0
            continue
        index+=1
        all_article += str(table)
    try:
        news = War(title=str(title), body=str(all_article), description=str(article_description), image=str(link_on_img))
        db.session.add(news)
        db.session.commit()
    except Exception as exp:
        db.session.rollback()
        print(str(title))
        print(exp)
        pass

def parse_all_links_from_war_news():
    url = "https://censor.net/war"
    req = requests.get(url)
    soups = BeautifulSoup(req.content, 'html.parser')
    artist_name_list = soups.find_all("h3")
    for i in artist_name_list:
        variable = (i.find('a')).get('href')
        parse_all_news_from_war_links(variable)
parse_all_links_from_war_news()





# parse_all_news_from_war_links("https://censor.net/ru/news/3221501/voyina_v_nagornom_karabahe_azerbayidjan_initsiiruet_sozdanie_mejdunarodnogo_tribunala_armeniya_obratilas#comments")

# p = requests.get(
#     'https://storage1a.censor.net/images/f/0/8/5/f085a44c14baf65c7af23d8cdedd1537/censor_news_big3.jpg')
# out = open(".war.jpg", "wb")
# out.write(p.content)
# out.close()
