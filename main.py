import re

import requests
import json
from article import Article
from bs4 import BeautifulSoup

BASE_URL = 'https://nl.pepper.com/?'
PARAMS = {"page": "1",
          "ajax": "true",
          "layout": "horizontal",
          }

ARTICLES = []


def filter_category(category_name):
    return None


def change_page(page_number):
    PARAMS["page"] = str(page_number)


def get_new_page_data():
    req = requests.get(url=BASE_URL, params=PARAMS)
    data = req.json()['data']['content']
    return data


def parse_pages(product):
    soup = BeautifulSoup(product, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        ARTICLES.append(parse_article(article))
    return None


def parse_article(article):
    # article_object = Article(
    #     article.get('id')
    #
    # )
    print(article.prettify())
    id = article.get('id').removeprefix('thread_')
    temperature = article.find('span', class_='vote-temp').text.strip()
    merchant = article.find('span', class_='cept-merchant-name').text.strip()
    promotion_type = article.find('span', class_='cept-merchant-link-term').next.nextSibling.strip()
    short_description = article.find('div', class_='cept-description-container').text.strip()
    return None


if __name__ == '__main__':
    for i in range(1, 3):
        change_page(i)
        page = get_new_page_data()
        parse_pages(page)
        print(i)
