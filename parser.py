import requests
import random
from bs4 import BeautifulSoup

class Announcement:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date


class Parser:
    def __init__(self): #TODO
        pass
    
    def get_html(self, url, useproxy=False):
        headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
        if useproxy==True:
            proxies = [i.strip('\n').split(',') for i in open('proxy-list.txt')]
            random.shuffle(proxies)
            requests.get(url, proxies={"http": proxies[0][0]}, headers=headers)
        else:
            requests.get(url, headers=headers)

    def parse(self):   #TODO
        pass
