
    
    
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import threading
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("stockTest.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pushOn.clicked.connect(self.onPush)
        self.pushOff.clicked.connect(self.offPush)
        self.flag = True
    #btn_1이 눌리면 작동할 함수
    def onPush(self) :
       
        print(self.plainTextEdit.toPlainText() )
        t1= threading.Thread(target=self.myrun)
        t1.start()
       
    def offPush(self):
        print("off")
        self.flag = False
        self.t1.stop()
        self.lbl.setText("검색 멈춤")
    
    def myrun(self):
        while self.flag == True:
            self.lbl.setText("검색 중")
                
            options = Options()
            options.headless = True
            browser = webdriver.Chrome(executable_path="D:\chromedriver.exe", options=options)
            browser.get("https://finance.daum.net/quotes/A"+self.plainTextEdit.toPlainText()+"#current/quote")
            
            time.sleep(3)
            price = browser.find_element_by_css_selector("strong[data-realtime-trade-price=yes]")
            name = browser.find_element_by_css_selector("#favorite")
            code = browser.find_element_by_css_selector("#favorite em")
            gtime = browser.find_element_by_css_selector("#marketStatus") 
    
            
            print(price.text)
            print(name.text[1:-6])
            print(code.text)
            print(str(datetime.today())[0:11] + gtime.text[0:5])
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()