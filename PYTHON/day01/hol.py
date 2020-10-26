import random


mine = input("홀짝을 입력하세요 : ")

rnd = random.random() 

result = ""
if rnd >= 0.5 :
    com = "홀"
else :
    com = "짝"
    
print ("com : {}".format(com) )
print ("나: {}".format(mine) )
    
if mine == com :
    print("이겼습니다.")
else :
    print("졌습니다.")