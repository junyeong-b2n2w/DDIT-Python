import time

from bs4 import BeautifulSoup
import requests
import json
import pymysql

url = "https://finance.daum.net/api/quote/A005930/days?symbolCode=A005930&page=1&perPage=10&pagination=true"
headers = {
            'Referer': 'http://finance.daum.net',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.127'
}




con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "Insert into stock (cname, ccode, price, gtime) values (%s,%s,%s,%s )" 



while(True):
    
    time.sleep(1)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    
    
    
    jsonObj = response.json()
    
    JsonData = json.dumps(jsonObj,indent=4)
    print(jsonObj.get("data")[0])
    print(jsonObj.get("data")[0].get("date"))
    print(jsonObj.get("data")[0].get("symbolCode"))
    print(jsonObj.get("data")[0].get("tradePrice"))
    
    cname = "삼성전자"
    gtime = jsonObj.get("data")[0].get("date")
    ccode = jsonObj.get("data")[0].get("symbolCode")
    price = jsonObj.get("data")[0].get("tradePrice")

    cur.execute(sql, (cname,ccode,price,gtime))
    
    con.commit()
    
    
con.close()
