import time

from bs4 import BeautifulSoup
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

#course_dep = input("Enter the course department : ")
#course_code = input("Enter the course code : ")
#course_dep = course_dep.upper()

driver = webdriver.Chrome(PATH)

driver.get("https://stars.bilkent.edu.tr/evalreport/index.php?mode=scn&semCode=20101&crsCode=ENG&crsNum=101&brCode=114")
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
tags = soup.find_all(class_ = "dataTable")
start = False
for tag in tags:
    tag = tag.text.split()
    if tag[0] == "AVERAGES":
        start = True
        print((float(tag[21].replace(",",".")) + float(tag[32].replace(",","."))) / 2)
        break


"""
soup = BeautifulSoup(page_source, 'lxml')
tags = soup.find_all('tr', id =lambda x: x and x.startswith(course_dep))
terms = {"Fall": 1, "Spring": 2, "Summer": 3}
for tag in tags:
    tag = tag.text.split()
    courseYear = tag[0][:4]
    courseTerm = terms.get(tag[1])
    sectionCode = tag[3][tag[3].find("-") + 1:].lstrip("0")

    try:
        driver.execute_script(f"javascript:openEvalPageForSection('{courseYear}{courseTerm}', '{course_dep}', '{course_code}', '{sectionCode}')")
    except:
        pass
    time.sleep(3)
    #javascript: openEvalPageForSection('20211', 'CS', '102', '1')

"""
"""
driver.get("https://stars.bilkent.edu.tr/homepage/courses.php?DEPT=CS")
time.sleep(10)

page_src = driver.page_source
soup = BeautifulSoup(page_src, 'lxml')
tags = soup.find_all('tr')
depNames = []
start = False
for tag in tags[:-1]:
    tag = tag.text.split()
    if(start):
        depNames.append(tag[0])
    if tag[0] == "Course":
        start = True

print(depNames)

"""
"""
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