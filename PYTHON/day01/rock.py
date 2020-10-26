import random


mine = input("가위바위보를 입력하세요 : ")

rnd = random.random() 

result = ""
if rnd >= 0.6666666666 :
    com = "가위"
elif rnd >= 0.333333333 :
    com = "바위"
else :
    com = "보"
    
print ("com : {}".format(com) )
print ("나: {}".format(mine) )
  

if mine == "가위" and com == "바위" or mine == "바위" and com == "보" or mine == "보" and com == "가위"  :
    print("졌습니다.")
elif mine == "보" and com == "바위" or mine == "가위" and com == "보" or mine == "바위" and com == "가위"  :
    print("졌습니다.")
elif mine == com:
    print("비겼습니다.")
else :
    print("입력이 잘못되었습니다.")