import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("04.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.sumNums)
       

    #btn_1이 눌리면 작동할 함수
    def sumNums(self) :
        num1 = int(self.te1.toPlainText())
        num2 = int(self.te2.toPlainText())
        
        total=0
        
        for i in range(num1, num2+1):
            total = total + i
        
        self.te3.setPlainText(str( total ))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()