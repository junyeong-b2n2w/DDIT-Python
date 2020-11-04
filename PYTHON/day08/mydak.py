import requests
from bs4 import BeautifulSoup
import time
import telegram

url = "https://www.jinsimdak.com/home/product/detail.php?prdcode=G1000000326"


token = 'MY_TOKEN'

bot = telegram.Bot(token=token)

chat_id = 'MYChatID'

num = 0;
while True:
    num +=1
    
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text
    
        soup = BeautifulSoup(html, 'html.parser')
        
        btn_box = soup.select_one('.btn-box')
        
        text = btn_box.select_one('.orange').text
        print(text)
        
        now = time.localtime()    
        
        outText= "진심닭컴 염통 입고\n" +  "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        
        print(num)
        if text != "품절" : bot.sendMessage(chat_id = chat_id, text=outText )
        time.sleep(300)
    except:
        time.sleep(300)
        pass
    
    
