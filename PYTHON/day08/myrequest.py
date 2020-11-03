import time

from bs4 import BeautifulSoup
import requests


url = "http://192.168.43.123/JAVASCRIPT/list.html"


response = requests.get(url)
response.encoding = 'utf-8'

html = response.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.find_all('tr')

for title in my_titles:
    titles = title.find_all('td')
    print(titles[0].text , "  // " , titles[1].text)




