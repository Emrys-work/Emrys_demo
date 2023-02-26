from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

sleep(1)

element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
element.send_keys('您好')

sleep(1)

wd.quit()
