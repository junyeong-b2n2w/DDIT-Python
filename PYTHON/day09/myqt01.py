
    
    
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import threading
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.chgLbl)
       

    #btn_1이 눌리면 작동할 함수
    def chgLbl(self) :
       
        t1= threading.Thread(target=self.myrun)
        t1.start()
       
        
    def myrun(self):
        for i in range(100):
            time.sleep(1)
            num = int(self.label.text())
            num = num+1
            
            self.label.setText(str(num))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()