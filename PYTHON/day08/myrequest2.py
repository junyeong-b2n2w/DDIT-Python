import time

from bs4 import BeautifulSoup
import requests
import pymysql

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "Insert into mytable (col02, col03) values (%s,%s )" 



url = "http://192.168.43.123/JAVASCRIPT/list.html"


response = requests.get(url)
response.encoding = 'utf-8'

html = response.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.find_all('tr')

for title in my_titles:
    titles = title.find_all('td')
    print(titles[0].text , "  // " , titles[1].text)
    cur.execute(sql,(titles[0].text,titles[1].text))






con.commit()

con.close()

