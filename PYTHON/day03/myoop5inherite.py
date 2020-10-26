class Animal:
    def __init__(self):
        self.age = 1
    def getOld(self):
        self.age += 1
    
class God:
    def __init__(self):
        self.sprit_power = 1
    def goToGeryong(self):
        self.sprit_power += 10
    def goToMinsokchon(self):
        self.sprit_power += 2
 
    
class Human(Animal ,God):
    def __init__(self):
        super().__init__()
        God.__init__(self)
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
    
    def __str__(self):
        return str(self.age)  + " / " + str(self.money_power) +" / " + str(self.sprit_power)    


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
    
    print(b.sprit_power)
    b.goToGeryong()
    b.goToMinsokchon()
    print(b.sprit_power)
    
    print(b.__str__())
    print(b)
    
    