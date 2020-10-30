import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QLabel, Qt, QRect, QSize
from PyQt5.uic.Compiler.qtproxies import QtGui
from PyQt5.QtGui import QIcon

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
        
        self.lbl2D = []
        
        for i in range(0,len(self.arr2D)):
            line = []
            for j in range(0,len(self.arr2D[i])):
                button = QPushButton("",self)
                #button.setObjectName(name)
                button.clicked.connect(lambda i,j: print( self.arr2D[i][j]) )
                button.setIcon(QIcon('0.png'))
                button.setIconSize(QSize(40,40))
                button.setGeometry(j*40,i*40,40,40)
                button.show()
                line.append(button)
            self.lbl2D.append(line)
        
        self.myrender()
        
        
        
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.btn_clicked)
        

    #btn_1이 눌리면 작동할 함수
    def btn_clicked(self) :

        self.myrender()
    
        
    def handleButton(self):
        print(self.sender())
        
    def myrender(self):
        for i in range(0,len(self.lbl2D)):
            for j in range(0,len(self.lbl2D[i])):
                if( self.arr2D[i][j] == 1): self.lbl2D[i][j].setIcon(QIcon('1.png'))
                if( self.arr2D[i][j] == 2): self.lbl2D[i][j].setIcon(QIcon('2.png'))
                
    
    
        
    
 
        

    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()