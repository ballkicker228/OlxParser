from selenium import webdriver
import random
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class Announcement:
    def __init__(self, name, price, date, address, status):
        self.name = name
        self.price = price
        self.date = date
        self.address = address
        self.status = status

class Category:
    def __init__(self, name):
        self.category = f"https://www.olx.kz/{name}"


class Parser:
    def __init__(self): #TODO
        pass 

    def parse(self, category: Category):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options) 
        driver.get(category.category)
        listofannouncementsdriver = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[5]/div/div[2]')
        announcementslist = listofannouncementsdriver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for announcement in announcementslist:
            link = announcement.find_element(By.CLASS_NAME, "css-rc5s2u")
            print(link.get_attribute("href"))
            print("\n ---------------------\n")
        #print(html)
