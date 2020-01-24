import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get('https://oxylabs.io/products/real-time-crawler')

keyword = driver.find_element_by_name("keyword")
keyword.send_keys('Aditya Chavan')
sleep(0.5)

keyword.submit()
contentString=""
while len(contentString)<25:
    contentString = driver.find_element_by_tag_name("pre").text

driver.quit()

#Analysis of contentString
url=''
source=''
for i in range(len(contentString)):
    if contentString[i]=='u' and contentString[i+1]=='r' and contentString[i+2]=='l' and contentString[i+3]=='"' and contentString[i+4]==':':
        for j in range(i+7, len(contentString)):
            url+=contentString[j]
            if contentString[j]=='"':
                break
    if contentString[i]=='s' and contentString[i+1]=='o' and contentString[i+2]=='u' and contentString[i+3]=='r' and contentString[i+4]=='c' and contentString[i+5]=='e' and contentString[i+6]=='"':
        for j in range(i+10, len(contentString)):
            source+=contentString[j]
            if contentString[j]=='"':
                break

url=url.split("\"")

source=source.split('"')

url=url+source
z=''
url=set(url)
url=list(url)
url.remove(z)
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXX')
# print(url)
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXX')

#Removing Social Sites
urlNoSocial=[]
social=['facebook', 'twitter','linkedin','youtube','google','Youtube']
for e in url:
    for s in social:
        if s in e:
            break
    else:
        urlNoSocial.append(e)
        
for i in urlNoSocial:
    print(i)

