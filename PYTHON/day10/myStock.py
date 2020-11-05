import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="D:\chromedriver.exe", options=options)
browser.get("https://finance.daum.net/quotes/A005930#current/quote")

time.sleep(3)
price = browser.find_element_by_css_selector("strong[data-realtime-trade-price=yes]")
name = browser.find_element_by_css_selector("#favorite")
code = browser.find_element_by_css_selector("#favorite em")
gtime = browser.find_element_by_css_selector("#marketStatus") 




print(price.text)
print(name.text[1:-6])
print(code.text)
print(str(datetime.today())[0:11] + gtime.text[0:5])
 


