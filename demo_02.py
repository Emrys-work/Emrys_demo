from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(10)


wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

element = wd.find_element(By.CSS_SELECTOR,
                          '#s_radio input[name="teacher"]:checked')

print(element.get_attribute('value'))

time.sleep(1)

wd.find_element(By.CSS_SELECTOR, '#s_radio input[value="小雷老师"]').click()

time.sleep(1)

wd.quit()
