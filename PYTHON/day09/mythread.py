from threading import Thread


def print_num():
    for i in range(10000):
        print(str(i) , end=' ')
        if i %100 ==0:
            print()

def print_char():
    for i in range(10000):
        print(chr(i), end=' ')
        if i %100 ==0:
            print()
        
t= Thread(target=print_num)
t1= Thread(target=print_char)
t.start()
t1.start()
