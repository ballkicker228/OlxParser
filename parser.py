from selenium import webdriver
import random
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class Announcement:
    def __init__(self, *, name, price, date, address, status, link):
        self.name = name
        self.price = price
        self.date = date
        self.address = address
        self.status = status
        self.link = link

class Category:
    def __init__(self, name):
        self.category = f"https://www.olx.kz/{name}"


class Parser:
    def __init__(self): #TODO
        pass 

    def parse(self, category: Category):
        links = []
        announcementslist = []
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options) 
        driver.get(category.category)
        listofannouncementsdriver = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[5]/div/div[2]')
        announcementslistdiv = listofannouncementsdriver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for announcementdiv in announcementslistdiv:
            
            link = announcementdiv.find_element(By.CLASS_NAME, "css-rc5s2u").get_attribute("href")
            

            #announcementslist.append(Announcement(name=name, price=price, date=date, address=address, status=status, link=link))
        
        print(links)
