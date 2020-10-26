class Animal:
    def __init__(self):
        self.age = 1
    def getOld(self):
        self.age += 1
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money_power = 100000
    def earnMoney(self,i=1):
        if i == 'none':
            self.money_power += 1
        else:
            self.money_power += i
        print(i)
        self.money_power += i
    def getOld(self):
        self.age += 2
    


if __name__ == '__main__':
   
    b= Human()
    print(b.age)
    b.getOld()
    print(b.money_power)
    
    b.earnMoney()
    print(b.money_power)
    b.earnMoney(6)
    print(b.money_power)
    
    print(b.age)
    
    