import time

from bs4 import BeautifulSoup
import requests


url = "https://money2.daishin.com/E5/WTS/Search/TotalSearch.aspx?m=1194&p=3669&v=3114&word=7IK87ISx7KCE7J6Q"


response = requests.get(url)
response.encoding = 'utf-8'

html = response.text

print(html)



