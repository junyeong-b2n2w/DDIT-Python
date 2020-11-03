import os
import sys
import urllib.request

import pymysql
from bs4 import BeautifulSoup

q = input("검색어 입력 >")
client_id = "rX_L_G9st7EbCVN81nrm"
client_secret = "dAoD5Xbg_m"
encText = urllib.parse.quote(q)
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body=""
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

soup = BeautifulSoup(response_body, 'lxml')

my_items = soup.find_all('item')

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "Insert into naver (title, link,description,bloggername, bloggerlink,postdate) values (%s,%s,%s,%s,%s,%s )"
 

for item in my_items:
    print(item.find('title').text)
    print(item.find('link').text)
    print(item.find('description').text)
    print(item.find('bloggername').text)
    print(item.find('bloggerlink').text)
    print(item.find('postdate').text)
    
    title = item.find('title').text
    link_1 = item.find('link').text
    description = item.find('description').text
    bloggername = item.find('bloggername').text
    bloggerlink = item.find('bloggerlink').text
    postdate = item.find('postdate').text
    
    cur.execute(sql , (title,link_1,description,bloggername, bloggerlink, postdate))




con.commit()

con.close()
