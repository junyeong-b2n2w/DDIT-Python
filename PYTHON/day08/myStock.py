import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="D:\chromedriver.exe", options=options)
browser.get("https://finance.daum.net/quotes/A005930#current/quote")

time.sleep(3)
tag_names = browser.find_element_by_id("boxSummary").find_elements_by_class_name("pR")
tag_names = browser.find_element_by_tag_name("table")
print(tag_names.text[1:5])
print(tag_names.text[5:11])
a,b = tag_names.text[16:22].split(",")
print(a+b)

print(tag_names)


