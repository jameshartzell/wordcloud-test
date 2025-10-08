import requests as rq
from selenium import webdriver
from selenium.webdriver.common.by import By
from requests_html2 import HTMLSession

url = 'https://justmytoots.com/@bimmer@mastodon.social'

#wd = webdriver.Chrome()
#wd.get(url)
#stuff = wd.find_element(By.XPATH, "/html/body").text
#wd.close()

s = HTMLSession()
bitch = s.get(url)
print(bitch.text)
stuff = str(bitch.html)

with open('asdf.html','w') as f:
    f.write(stuff)
    f.close()
