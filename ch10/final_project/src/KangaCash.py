from src import shop
s = shop.Shops()
class Cash:
    def __init__(self):
        with open(r"etc\KangaCash.txt") as file:
            self.KangaCash = int(file.read())
    def addCash(self, cash):
        petEchidna = s.echidna() #this always returns False, and I don't know why. It works in the movement module. I'm literally crying rn
        hat = s.hat()
        lights = s.prettylights()
        self.cash = cash
        self.multiplier = 0
        if lights == True:
            self.multiplier += .15
        if hat == True:
            self.multiplier += .1
        self.cash = self.cash*self.multiplier + self.cash
        if petEchidna == True:
            self.cash += 5
        self.KangaCash = self.KangaCash + self.cash 
        if self.cash < 0:
            self.cash = 0
        with open(r"etc\KangaCash.txt","w") as file:
            file.write(str(self.KangaCash))
