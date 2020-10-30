
    
    
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QLabel, Qt, QRect

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        self.arr2D = [ 
                        [1,0,0,0,0, 0,0,0,0,0],
                        [0,1,0,0,0, 0,0,0,0,0],
                        [0,0,2,2,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
            
                        ]

        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.btn_clicked)
        

    #btn_1이 눌리면 작동할 함수
    def btn_clicked(self) :
        self.printArr2D()
        
        
        
      
        
        
        for i in range(0,len(self.arr2D)):
            for j in range(0,len(self.arr2D[i])):
                label2 = QLabel("name",self)
                #label2.setObjectName(name)
                img = "0.png"
                if( self.arr2D[i][j] == 1): img = "1.png"
                if( self.arr2D[i][j] == 2): img = "2.png"
                label2.setPixmap(QPixmap(QPixmap(img)))
                label2.setGeometry(QRect(j*40,i*40,40,40))
                label2.show()
    
        
        
    def printArr2D(self):
        print(self.arr2D[0])
        print(self.arr2D[1])
        print(self.arr2D[2])
        print(self.arr2D[3])
        print(self.arr2D[4])
        print(self.arr2D[5])
        print(self.arr2D[6])
        print(self.arr2D[7])
        print(self.arr2D[8])
        print(self.arr2D[9])

    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()