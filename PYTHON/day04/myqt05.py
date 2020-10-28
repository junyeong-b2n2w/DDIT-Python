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
        self.bt1.clicked.connect(self.btf)
        self.bt2.clicked.connect(self.btf)
        self.bt3.clicked.connect(self.btf)
        self.bt4.clicked.connect(self.btf)
        self.bt5.clicked.connect(self.btf)
        self.bt6.clicked.connect(self.btf)
        self.bt7.clicked.connect(self.btf)
        self.bt8.clicked.connect(self.btf)
        self.bt9.clicked.connect(self.btf)
        self.bt0.clicked.connect(self.btf)
        self.bt_call.clicked.connect(self.call)
       
    def btf(self):
        self.line.setText(self.line.text() + self.sender().text())
        
    def call(self) :
        QMessageBox.about(self,"전화걸어요 ~",self.line.text() +  "로 전화거는중")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()