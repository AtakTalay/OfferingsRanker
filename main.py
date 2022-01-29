import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions

PATH = "C:\Program Files (x86)\chromedriver.exe"

course_dep = input("Enter the course department : ")
course_code = input("Enter the course code : ")
course_dep = course_dep.upper()

driver = webdriver.Chrome(PATH)
driver.get("https://stars.bilkent.edu.tr/homepage/plain_offerings")

time.sleep(10)
try:
    driver.execute_script(f"javascript:openOldOfferingsPage('{course_dep} {course_code}')")
except:
    pass

time.sleep(1)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
tags = soup.find_all('tr', id =lambda x: x and x.startswith(course_dep))
for tag in tags:
    print(tag.text.split())