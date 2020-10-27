import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("05.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.bt1.clicked.connect(self.bt1f)
        self.bt2.clicked.connect(self.bt2f)
        self.bt3.clicked.connect(self.bt3f)
        self.bt4.clicked.connect(self.bt4f)
        self.bt5.clicked.connect(self.bt5f)
        self.bt6.clicked.connect(self.bt6f)
        self.bt7.clicked.connect(self.bt7f)
        self.bt8.clicked.connect(self.bt8f)
        self.bt9.clicked.connect(self.bt9f)
        self.bt0.clicked.connect(self.bt0f)
        self.bt_call.clicked.connect(self.call)
       

   
        
    def bt1f(self) :
        self.line.setText(self.line.text() + "1")
    def bt2f(self) :
        self.line.setText(self.line.text() + "2")
    def bt3f(self) :
        self.line.setText(self.line.text() + "3")
    def bt4f(self) :
        self.line.setText(self.line.text() + "4")
    def bt5f(self) :
        self.line.setText(self.line.text() + "5")
    def bt6f(self) :
        self.line.setText(self.line.text() + "6")
    def bt7f(self) :
        self.line.setText(self.line.text() + "7")
    def bt8f(self) :
        self.line.setText(self.line.text() + "8")
    def bt9f(self) :
        self.line.setText(self.line.text() + "9")
    def bt0f(self) :
        self.line.setText(self.line.text() + "0")
    def call(self) :
        
        QMessageBox.about(self,"전화걸어요 ~",self.line.text() +  "로 전화거는중")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()