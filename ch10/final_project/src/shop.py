from src import text
import random
from src import username
Shop = [
    "Pretty Lights",
    "Overcharged Space Canons",
    "Reinforced Doors",
    "Shiny Petrol",
    "A Pretty Bow",
    "A Cool Hat",
    "Sonic Speed WiFi",
    "New Windshield Wipers",
    "A Platypus Poster?", 
    "Powered Steering Wheel",
    "Pet Echidna"
]
Shop_Descriptions = {
    "Pretty Lights":("Equipping these lights will earn you 15% more KangaCash","while in use. (Only one decoration may be in use at a time.)","",""),
    "Overcharged Space Canons":("Firing these space cannons will shoot you ahead two spaces.","","",""),
    "Reinforced Doors":("These doors will prevent you from going up to one space","backwards on your turn.","",""),
    "Shiny Petrol":("The shininess will take you twice as many spaces on your turn in style.","","",""),
    "A Cool Hat":("Your coolness will earn you 10% more KangaCash while equipped.","(Only one piece of headwear may be equipped at a time.)","",""),
    "A Pretty Bow":("Your prettiness will give you a 15% chance to move an extra","space while equipped. (Only one piece of headwear","may be equipped at a time.)",""),
    "Sonic Speed WiFi":("Your fast WiFi will take you an extra space further on","your turn.","",""),
    "New Windshield Wipers":("Your clear vision will allow you to reverse any","backwards movement you would have encountered on your turn.","",""),
    "A Platypus Poster?":("A mysterious poster of a teal platypus in a fedora.","This poster will give you a 10% chance to move","an extra space while in use. (Only one decoration may be in use at a time.)",""),
    "Powered Steering Wheel":("This steering wheel will allow you to move up to","four spaces in any direction of your choice for your turn.","",""),
    "Pet Echidna":("This golden echidna will bring you both joy and 5 KangaCash","per turn.","","")
}
Shop_Prices = {
    "Pretty Lights":20,
    "Overcharged Space Canons":25,
    "Reinforced Doors":15,
    "Shiny Petrol":30,
    "A Cool Hat":20,
    "A Pretty Bow":30,
    "Sonic Speed WiFi":25,
    "New Windshield Wipers":25,
    "A Platypus Poster?":20,
    "Powered Steering Wheel":50,
    "Pet Echidna": 55
}
with open(r"etc\KangaCash.txt") as file:
    KC = int(file.read())
class Shops:
    def __init__(self):
        self.pet = []
        self.your_inventory = []
        self.active_item = []
        self.headwear = []
        self.decor = []
        self.petechidna = False
        self.prettybow = False
        self.coolhat = False
        self.lights = False
        self.platypus = False
        self.canons = False
        self.doors = False
        self.petrol = False
        self.wifi = False
        self.wipers = False
        self.wheels = False
        num = len(Shop)
        num1 = int(random.randrange(0,num))
        num2 = int(random.randrange(0,num))
        while num1 == num2:
            num2 = int(random.randrange(0,num))
        num3 = int(random.randrange(0,num))
        while num3 == num1:
            num3 = int(random.randrange(0,num))
            while num3 == num2:
                num3 = int(random.randrange(0,num))
        while num3 == num2:
            num3 = int(random.randrange(0,num))
            while num3 == num1:
                num3 = int(random.randrange(0,num))
        self.pick1 = Shop[num1]
        self.pick2 = Shop[num2]
        self.pick3 = Shop[num3]
    def entershop(self):
        with open(r"etc\current_space.txt") as file:
            self.current_space = int(file.read())
        if self.current_space == 7 or self.current_space == 15 or self.current_space == 27 or self.current_space == 32:
            words = text.Text(("Welcome to the shop. Would you like to look around?","","","Press 'y' for yes, or 'n' to continue on."))
            words.usergiveinput()
            decision = words.choices()
            if decision == 'y':
                self.shop()
            elif decision == 'n':
                words = text.Text(("Okay, maybe next time!","","",""))
                words.usergiveinput()
            else:
                words = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
                words.usergiveinput()
                self.entershop()
    def shop(self):
        u = username.Username()
        name = u.username()
        words = text.Text(("Hi, " + name + "! Here are today's goods:", self.pick1, self.pick2, self.pick3))
        words1 = text.Text(("Press 'a' to view or purchase '" + self.pick1 + "',","'b' to view or purchase '" + self.pick2 + "', ","'c' to view or purchase '" + self.pick3 + "', or ","'enter' to exit the shop."))
        words2 = text.Text(("Okay, maybe next time!","","",""))
        words.regulartext("True")
        words1.usergiveinput()
        self.decision = words1.choices()
        if self.decision == 'a' or self.decision == 'b' or self.decision == 'c':
            self.view()
        elif self.decision == ' ':
            words2.regulartext("True")
        else:
            words = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
            words.regulartext("True")
            self.shop()
    def view(self):
        words = text.Text(("Would you like to purchase this item?","Press 'y' to purchase this item,","'n' to view other items,","or 'enter' to exit the shop."))
        words1 = text.Text(("Cost: " + str(Shop_Prices[self.pick1]) + " KangaCash","","",""))
        words2 = text.Text(("Cost: " + str(Shop_Prices[self.pick2]) + " KangaCash","","",""))
        words3 = text.Text(("Cost: " + str(Shop_Prices[self.pick3]) + " KangaCash","","",""))
        words4 = text.Text(Shop_Descriptions[self.pick1])
        words5 = text.Text(Shop_Descriptions[self.pick2])
        words6 = text.Text(Shop_Descriptions[self.pick3])
        words7 = text.Text(("Okay, maybe next time!","","",""))
        if self.decision == 'a':
            words4.regulartext("True")
            words1.regulartext("True")
            self.choice = self.pick1
        elif self.decision == 'b':
            words5.regulartext("True")
            words2.regulartext("True")
            self.choice = self.pick2
        elif self.decision == 'c':
            words6.regulartext("True")
            words3.regulartext("True")
            self.choice = self.pick3
        else:
            self.shoperror()
        words.usergiveinput()
        self.decision1 = words.choices()
        if self.decision1 == 'y':
            self.purchase()
        elif self.decision1 == 'n':
            self.shop()
        elif self.decision1 == ' ':
            words7.regulartext("True")
        else:
            self.shoperror()
    def purchase(self):
        with open(r"etc\KangaCash.txt") as file:
            KangaCash = int(file.read())
        if int(KangaCash) >= int(Shop_Prices[self.choice]):
            KangaCash -= Shop_Prices[self.choice]
            with open(r"etc\KangaCash.txt","w") as file:
                file.write(str(KangaCash))
            if self.choice == "Pet Echidna":
                if len(self.pet) > 0:
                    words = text.Text(("Sorry, you may not have more than one pet echidna.","Your old pet has been set free to make room for your new one.","Animals raised in captivity do not do well in the wild, but you do not care.","Press 'enter' to continue."))
                else:
                    self.pet.append(self.choice)
                    words = text.Text(("Adventures await! Your pet echidna has joined you on the board.","","","Press 'enter' to continue."))
                self.petechidna = True
            elif self.choice == "A Pretty Bow" or self.choice == "A Cool Hat":
                if len(self.headwear) > 0:
                    if self.headwear[0] == "A Pretty Bow":
                        hat = "bow"
                        self.prettybow = False
                    else:
                        hat = "hat"
                        self.coolhat = False
                    if self.choice == "A Pretty Bow":
                        newhat = "bow"
                        self.prettybow = True
                    else:
                        newhat = "hat"
                        self.coolhat = True
                    self.headwear.remove(self.headwear[0])
                    self.headwear.append(self.choice)
                    words = text.Text(("Sorry, you may not wear more than one thing on your head at a time.","Your head is simply not big enough.","You remove your " + hat + " and put on your new " + newhat + ".","Press 'enter' to continue."))
                else:
                    if self.choice == "A Pretty Bow":
                        newhat = "bow"
                        self.prettybow = True
                    else:
                        newhat = "hat"
                        self.coolhat = True
                    self.headwear.append(self.choice)
                    words = text.Text(("Awesome! Check out your new look!","","","Press 'enter' to continue."))
            elif self.choice == "Pretty Lights" or self.choice == "A Platypus Poster?":
                if len(self.decor) > 0:
                    if self.decor[0] == "Pretty Lights":
                        decor = "pretty lights"
                        self.lights = False
                    else:
                        decor = "platypus poster"
                        self.platypus = False
                    if self.choice == "Pretty Lights":
                        newdecor = "pretty lights"
                        self.lights = True
                    else:
                        newdecor = "platypus poster"
                        self.platypus = True
                    words = text.Text(("Sorry, you may not have more than one decoration at a time.","You take down your " + decor + ",","and you replace it with your new " + newdecor + ".","","Press 'enter' to continue."))
                else:
                    if self.choice == "Pretty Lights":
                        newdecor = "pretty lights"
                        self.lights = True
                    else:
                        newdecor = "platypus poster"
                        self.platypus = True
                    words = text.Text(("You hang up your new " + newdecor + ".","Your time machine is looking super bonza.","",""))
                self.decor.append(self.choice)
            else:
                if len(self.your_inventory) >= 3:
                    words1 = text.Text(("Sorry, you may not have more than three inactive items in your","inventory at a time. Please discard one.","","Press 'enter' to continue."))
                    words1.regulartext("True")
                    words2 = text.Text(("Press 'a' to discard " + self.your_inventory[0], "'b' to discard " + self.your_inventory[1], "or 'c' to discard " + self.your_inventory[2], ""))
                    words2.usergiveinput()
                    decision = words2.choices()
                    if decision == 'a':
                        self.your_inventory.remove(self.your_inventory[0])
                    elif decision == 'b':
                        self.your_inventory.remove(self.your_inventory[1])
                    elif decision == 'c':
                        self.your_inventory.remove(self.your_inventory[2])
                    else:
                        words3 = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
                        words3.regulartext("True")
                        self.purchase()
                else:    
                    self.your_inventory.append(self.choice)
                    words = text.Text(("You now have " + self.your_inventory[-1] + " in your inventory.","","",""))
            words.regulartext("True")
        else:
            self.notEnoughCash()
    def shoperror(self):
        words = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
        words.regulartext("True")
        self.shop()
    def notEnoughCash(self):
        words = text.Text(("Sorry, you do not have enough KangaCash for this item.","","",""))
        words.regulartext("True")
        self.shop()
    def hat(self):
        return self.coolhat
    def bow(self):
        return self.prettybow
    def echidna(self):
        return self.petechidna
    def poster(self):
        return self.platypus
    def prettylights(self):
        return self.lights
    def items(self):
        return list(self.your_inventory)
    def asktoactivate(self):
        if len(self.your_inventory) == 0:
            words = text.Text(("You currently have no items to equip.","","","Press 'enter' to pick an event card."))
            words.regulartext("True")
        elif len(self.your_inventory) == 1:
            words = text.Text(("You have one item ready to be equipped.","Press 'y' to equip your " + self.your_inventory[0],"or press 'n' to wait until next turn.","Remember, this is a single-use item."))
            words.usergiveinput()
            decision = words.choices()
            if decision == 'y':
                item = self.your_inventory[0]
                self.activate(item)
            elif decision == 'n':
                words1 = text.Text(("Ok, maybe next time!","","",""))
                words1.regulartext("True")
            else:
                words1 = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
                words1.regulartext("True")
                self.asktoactivate()
        elif len(self.your_inventory) == 2:
            words = text.Text(("You have two single-use items ready to be equipped.","Press 'a' to equip your " + self.your_inventory[0],"'b' to equip your " + self.your_inventory[1], "or 'n' to wait until next turn."))
            words.usergiveinput()
            if decision == 'a':
                item = self.your_inventory[0]
                self.activate(item)
            elif decision == 'b':
                item = self.your_inventory[1]
                self.activate(item)
            elif decision == 'n':
                words1 = text.Text(("Ok, maybe next time!","","",""))
                words1.regulartext("True")
            else:
                words1 = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
                words1.regulartext("True")
                self.asktoactivate()
        elif len(self.your_inventory) == 3:
            words = text.Text(("You have three single-use items ready to be equipped.","Press 'a' to equip your " + self.your_inventory[0],"'b' to equip your " + self.your_inventory[1], "'c' to equip your " + self.your_inventory[2] + "or 'n' to wait until next turn."))
            words.usergiveinput()
            if decision == 'a':
                item = self.your_inventory[0]
                self.activate(item)
            elif decision == 'b':
                item = self.your_inventory[1]
                self.activate(item)
            elif decision == 'c':
                item = self.your_inventory[2]
                self.activate(item)
            elif decision == 'n':
                words1 = text.Text(("Ok, maybe next time!","","",""))
                words1.regulartext("True")
            else:
                words1 = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
                words1.regulartext("True")
                self.asktoactivate()
    def activate(self,item):   
        self.your_inventory.remove(item)
        self.active_item.append(item)
        if item == "Overcharged Space Canons":
            self.canons = True
        if item == "Reinforced Doors":
            self.doors = True
        if item == "Shiny Petrol":
            self.petrol = True
        if item == "Sonic Speed WiFi":
            self.wifi = True
        if item == "New Windshield Wipers":
            self.wipers = True
        if item == "Powered Steering Wheel":
            self.wheels = True
    def takeaway(self,item):
        self.active_item.remove(item)
        if item == "Overcharged Space Canons":
            self.canons = False
        if item == "Reinforced Doors":
            self.doors = False
        if item == "Shiny Petrol":
            self.petrol = False
        if item == "Sonic Speed WiFi":
            self.wifi = False
        if item == "New Windshield Wipers":
            self.wipers = False
        if item == "Powered Steering Wheel":
            self.wheels = False
    def canon(self):
        return self.canons
    def door(self):
        return self.doors
    def shiny(self):
        return self.petrol
    def sonic(self):
        return self.wifi
    def wiper(self):
        return self.wipers
    def wheel(self):
        return self.wheels
    