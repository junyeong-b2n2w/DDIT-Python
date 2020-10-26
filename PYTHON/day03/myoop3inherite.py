class Animal:
    def __init__(self):
        self.age = 1
    def getOld(self):
        self.age += 1
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money_power = 100000
    def earnMoney(self):
        self.money_power += 1
    


if __name__ == '__main__':
    a= Animal()
    print(a.age)

    a.getOld()
    
    print(a.age)
    
    b= Human()
    print(b.money_power)
    
    b.earnMoney()
    
    print(b.money_power)
    
    print(b.age)
    
    