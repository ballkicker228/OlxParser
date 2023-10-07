from selenium import webdriver
import random
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class Announcement:
    def __init__(self, *, name: str, price: int, date:int, address: str, link: str):
        self.name = name
        self.price = price
        self.date = date
        self.address = address
        self.link = link

class Category: #TODO filters
    def __init__(self, name, *, page=0):
        self.category = f"https://www.olx.kz/{name}"
        if page != 0:
            self.category = self.category + f"/?page={page}"


class Parser:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.options) 

    def parse_page(self, category: Category):
        announcementslist = [] 
        self.driver.get(category.category)
        listofannouncementsdriver = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[5]/div/div[2]')
        announcementslistdiv = listofannouncementsdriver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for announcementdiv in announcementslistdiv:
            
            link = announcementdiv.find_element(By.CLASS_NAME, "css-rc5s2u").get_attribute("href")
            name = announcementdiv.find_element(By.TAG_NAME, "h6").text
            price_address_date = announcementdiv.find_elements(By.TAG_NAME, "p")
            try:
                price = int(price_address_date[0].text.split(" тг")[0].replace(" ", ""))
            except ValueError:
                price = -1

            address, date = price_address_date[1].text.split(" - ")

            announcementslist.append(Announcement(name=name, price=price, date=date, address=address, link=link)) 
        
        return announcementslist

    def parse(self, category: Category):
        announcementslist = []
        self.driver.get(category.category)
        pagesnumber = int(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/div[5]/div/section[1]/div/ul/li[5]/a").text)
        for page in range(2, pagesnumber):
            url = Category(category.category[19:], page=page)
            print(url.category)
            anlist = self.parse_page(url)
            announcementslist = [*announcementslist, *anlist]
        return announcementslist

    def close(self):
        self.driver.close()
        del self
