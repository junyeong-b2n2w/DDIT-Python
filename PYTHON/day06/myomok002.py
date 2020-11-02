from os.path import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets

from PyQt5.Qt import QSize, QMessageBox

from_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.arr2D = [
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]
        self.setupUi(self)
        self.btn2D = []
        self.turn = True
        self.playing = True
        for i in range(len(self.arr2D)):
            line = []
            for j in range(len(self.arr2D[i])):
                btn = QtWidgets.QPushButton(self)
                btn.setAccessibleName(str(i)+","+str(j))
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40,40));
                btn.clicked.connect(self.btn_clicked)
                line.append(btn)
            self.btn2D.append(line)
        
        self.pb.clicked.connect(self.reset_click)
    
    def reset_click(self):
        self.arr2D = [
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]
        self.turn = True
        self.playing = True
        self.myrender()
        
    def myrender(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                if self.arr2D[i][j]==0 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("0.png"))
                elif self.arr2D[i][j]==1 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("1.png"))
                elif self.arr2D[i][j]==2 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("2.png"))
            
    def btn_clicked(self):
        if self.playing == False:
            return
        
        i = int(self.sender().accessibleName().split(",")[0])
        j = int(self.sender().accessibleName().split(",")[1])
        print(i , j)
        if self.arr2D[i][j] > 0 : 
            return
        
        self.arr2D[i][j] = (1 if self.turn  else 2)
        
        self.myrender()
        
        
        cntUp = self.getUp(i, j, 1 if self.turn  else 2)
        cntDw = self.getDw(i, j, 1 if self.turn  else 2)
        cntLe = self.getLe(i, j, 1 if self.turn  else 2)
        cntRi = self.getRi(i, j, 1 if self.turn  else 2)
        
        
        cntUL = self.getUL(i, j, 1 if self.turn  else 2)
        cntUR = self.getUR(i, j, 1 if self.turn  else 2)
        cntDL = self.getDL(i, j, 1 if self.turn  else 2)
        cntDR = self.getDR(i, j, 1 if self.turn  else 2)
        
        print(cntUp)
        print(cntDw)
        print(cntLe)
        print(cntRi)
        print(cntUL)
        print(cntUR)
        print(cntDL)
        print(cntDR)
        
        cnt01 = cntUp + cntDw + 1 ;
        cnt02 = cntLe + cntRi + 1 ;
        cnt03 = cntUL + cntDR + 1 ;
        cnt04 = cntUR + cntDL + 1 ;
        
        if cnt01 == 5 or cnt02 == 5 or cnt03 == 5 or cnt04 == 5:
            self.playing = False
            if(self.turn == True):
                QMessageBox.about(self,"결과","백돌 우승")
            else:
                QMessageBox.about(self,"결과","흑돌 우승")

            
        
        
        
        self.turn =  not self.turn
        
        
    def getUp(self, i, j ,idx):
        cnt = 0
        try:
            while(True):
                i = i-1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        return cnt
    
    
    def getDw(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                i = i+1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt
           
    def getLe(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                j = j-1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt 
        
    def getRi(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                j = j+1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt     
    
    def getUL(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                i = i+1
                j = j-1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt  
    
    
    
    def getUR(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                i = i+1
                j = j+1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt  
    
    def getDL(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                i = i-1
                j = j-1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt  
    
    
    def getDR(self, i, j ,idx):
        cnt = 0
        
        try:
            while(True):
                i = i-1 
                j = j+1
                if i < 0 : return cnt
                if j < 0 : return cnt
                if self.arr2D[i][j] == idx:
                    cnt = cnt + 1
                else : break
        except:
            pass
        
            
        return cnt  
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
