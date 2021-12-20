class Car (object):
    def __init__(self,model,color,company,speedlimit):
        self.color = color
        self.company = company
        self.model = model
        self.speedlimit = speedlimit
    def start(self):
        print('started')
        
    def stop(self):
        print('stoped') 
        
    def accelarate(self):
        print('accelarated')
        
ferrari = Car('5','red','ferrari','211')
print(ferrari.color)
ferrari.start()

class Icecream(object):
    def __init__(self,flavor,company,type):
        self.flavor = flavor
        self.company = company
        self.type = type
        
    def taste (self):
        print('Chocolate')
cornatto = Icecream('chocolate','quality walls','cornatto')        
print(cornatto.flavor)


        