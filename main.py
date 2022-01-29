import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions

PATH = "C:\Program Files (x86)\chromedriver.exe"

#course_dep = input("Enter the course department : ")
#course_code = input("Enter the course code : ")
#course_dep = course_dep.upper()

driver = webdriver.Chrome(PATH)


driver.get("https://stars.bilkent.edu.tr/homepage/courses.php?DEPT=CS")
time.sleep(10)
page_src = driver.page_source
soup = BeautifulSoup(page_src, 'lxml')
tags = soup.find_all('tr')
start = False
courseCodes = []
for tag in tags:
    tag = tag.text.split()
    if(tag[0] == "Courses"):
        start = False
    if (start):
        courseCodes.append(tag[0] + " " + tag[1])
    if (tag[-1] == "ECTS"):
        start = True
print(courseCodes)
"""

page_src = driver.page_source
soup = BeautifulSoup(page_src, 'lxml')
tags = soup.find_all('tr')
depNames = []
start = False
for tag in tags[:-1]:
    tag = tag.text.split()
    if(start):
        depNames.append(tag[0])
    if(tag[0] == "Course"):
        start = True

print(depNames)

"""
"""
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
    
"""