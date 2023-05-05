import pygame
import random
from src import ratio
from src import pause
from src import cards
from src import background
from src import text
from src import KangaCash
from src import shop
screen = pygame.display.set_mode()
p = pause.Pause()
s = shop.Shops()
class Movement:
    def __init__(self):
        r = ratio.Ratio()
        self.rat = r.fetchRatio()
        self.size = r.fetchSize()
        c = cards.Card()
        self.num = (self.size[0]/12)
        self.cardname = c.cardpick()
        self.space = int(c.cardspaces())
        self.description = c.carddescription()
        self.cash = int(c.cardsmoney())
        self.pet = s.echidna()
        KC = KangaCash.Cash()
        KC.addCash(self.cash)
        hat = s.hat()
        bow = s.bow()
        if bow == True:
            self.kangaroo1base = pygame.image.load(r'assets\Kangaroo1Bow.png').convert_alpha()
            self.kangaroo2base = pygame.image.load(r'assets\Kangaroo2Bow.png').convert_alpha()
            self.kangaroo3base = pygame.image.load(r'assets\Kangaroo3Bow.png').convert_alpha()
            self.kangaroo4base = pygame.image.load(r'assets\Kangaroo4Bow.png').convert_alpha()
            self.kangaroo5base = pygame.image.load(r'assets\Kangaroo5Bow.png').convert_alpha()
        elif hat == True:
            self.kangaroo1base = pygame.image.load(r'assets\Kangaroo1Hat.png').convert_alpha()
            self.kangaroo2base = pygame.image.load(r'assets\Kangaroo2Hat.png').convert_alpha()
            self.kangaroo3base = pygame.image.load(r'assets\Kangaroo3Hat.png').convert_alpha()
            self.kangaroo4base = pygame.image.load(r'assets\Kangaroo4Hat.png').convert_alpha()
            self.kangaroo5base = pygame.image.load(r'assets\Kangaroo5Hat.png').convert_alpha()
        else:
            self.kangaroo1base = pygame.image.load(r'assets\Kangaroo1.png').convert_alpha()
            self.kangaroo2base = pygame.image.load(r'assets\Kangaroo2.png').convert_alpha()
            self.kangaroo3base = pygame.image.load(r'assets\Kangaroo3.png').convert_alpha()
            self.kangaroo4base = pygame.image.load(r'assets\Kangaroo4.png').convert_alpha()
            self.kangaroo5base = pygame.image.load(r'assets\Kangaroo5.png').convert_alpha()
        self.echidnabase = pygame.image.load(r'assets\echidna.png').convert_alpha()
        self.echidna = pygame.transform.scale(self.echidnabase, (100*self.rat[0], 100*self.rat[1]))
        self.shopbase = pygame.image.load(r'assets\shop.png').convert_alpha()
        self.kangaroo1 = pygame.transform.scale(self.kangaroo1base,((300*self.rat[0]),(300*self.rat[1])))
        self.kangaroo2 = pygame.transform.scale(self.kangaroo2base,((300*self.rat[0]),(300*self.rat[1])))
        self.kangaroo3 = pygame.transform.scale(self.kangaroo3base,((300*self.rat[0]),(300*self.rat[1])))
        self.kangaroo4 = pygame.transform.scale(self.kangaroo4base,((300*self.rat[0]),(300*self.rat[1])))
        self.kangaroo5 = pygame.transform.scale(self.kangaroo5base,((300*self.rat[0]),(300*self.rat[1])))
        self.shop = pygame.transform.scale(self.shopbase,((500*self.rat[0]),(500*self.rat[1])))
        self.current_space_abs = self.currentspaceabsolute()
    def currentspaceabsolute(self):
        with open(r"etc\current_space.txt") as file:
            self.current_space = int(file.read())
        if self.current_space <= 5:
            self.current_space_abs = self.current_space
        elif self.current_space <= 11:
            self.current_space_abs = self.current_space - 6
        elif self.current_space <= 17:
            self.current_space_abs = self.current_space - 12
        elif self.current_space <= 23:
            self.current_space_abs = self.current_space - 18
        elif self.current_space <= 29:
            self.current_space_abs = self.current_space - 24
        elif self.current_space <= 35:
            self.current_space_abs = self.current_space - 30
        else:
            self.current_space_abs = self.current_space - 36
        return self.current_space_abs
    def spaces(self):
        s.asktoactivate()
        canons = s.canon()
        if canons == True:
            space = self.space
            self.space = 2
            words = text.Text(("Your overcharged space canons shoot you ahead 2 spaces.","","",""))
            self.hop()
            self.space = space
            s.takeaway("Overcharged Space Canons")
        wheel = s.wheel()
        if wheel == True:
            space = self.space
            words = text.Text(("Please enter a number between -4 and 4","","",""))
            words.numericalinput()
            self.space = int(words.numericaloutput())
            s.takeaway("Powered Steering Wheel")
            if self.space > 0:
                self.hop()
            else:
                self.flop()
            self.space = space
        wifi = s.sonic()
        if wifi == True:
            self.space += 1
            s.takeaway("Sonic Speed WiFi")
        petrol = s.shiny()
        if petrol == True:
            self.space *= 2
            s.takeaway("Shiny Petrol")   
        words = text.Text(("'" + self.cardname + "'","","",""))
        words.regulartext("True")        
        description = text.Text(self.description)
        description.regulartext("True")
        bow = s.bow()
        platypus = s.poster()
        if bow == True:
            pick = random.randrange(0,100)
            if pick < 15:
                self.space += 1
        if platypus == True:
            pick = random.randrange(0,100)
            if pick < 10:
                self.space += 1
        if self.space < 0:
            doors = s.door()
            if doors == True:
                self.space += 1
                s.takeaway("Reinforced Doors")
            wipers = s.wiper()
            if wipers == True:
                self.space = abs(self.space)
                s.takeaway("New Windshield Wipers")
            if self.space == -1:
                words = text.Text(("Kangaroo falls one space back.","","","Press 'enter' at any time to continue."))
            elif self.space == 0:
                words = text.Text(("Your items have prevented any backwards movement.","","","Press 'enter' at any time to continue."))
            elif self.space == 1:
                words = text.Text(("Your items have helped you out.","Kangaroo moves one space forward.","","Press 'enter' at any time to continue."))
            elif self.space > 1:
                words = text.Text(("Wow! Your items have really helped you out.","Kangaroo moves " + self.space + " spaces forward.","","Press 'enter' at any time to continue."))
            else:
                words = text.Text(("Kangaroo falls " + str(abs(self.space)) + " space back.","","","Press 'enter' at any time to continue."))
            words.regulartext("True")
            if self.space < 0:
                self.flop()
            elif self.space > 0:
                self.hop()
        elif self.space > 0:
            if self.space == 1:
                words = text.Text(("You move one space forward.","","","Press 'enter' at any time to continue."))
            else:
                words = text.Text(("You move " + str(self.space) + " spaces forward.","","","Press 'enter' at any time to continue."))
            words.regulartext("True")
            self.hop()
        else:
            words = text.Text(("You do not move.","","","Press 'enter' at any time to continue."))
            words.regulartext("True")
    def hop(self):
        count = 0
        x_coord = ((self.current_space_abs*self.num*2)-(100*self.rat[0]))
        while count < self.space:
            count += 1
            b = background.Background()
            self.bg = b.picture()
            location = b.shoplocation()
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo1,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.5)
            x_coord += self.num
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo2,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.5)
            self.current_space = self.current_space + 1
            with open(r"etc\current_space.txt", 'w') as file:
                file.write(str(self.current_space))
            reset_screen = b.reset()
            if reset_screen == True:
                self.current_space_abs = self.currentspaceabsolute()
                b = background.Background()
                self.bg = b.picture()
                location = b.shoplocation()
                self.current_space_abs = self.currentspaceabsolute()
                x_coord = ((self.current_space_abs*self.num*2)-(100*self.rat[0]))
                reset_screen = False
            else:
                x_coord += self.num
            s.entershop()
        with open(r"etc\current_space.txt", 'w') as file:
                file.write(str(self.current_space))
        screen.blit(self.bg,(0,-23))
        screen.blit(self.shop, location)
        self.petEchidna = s.echidna()
        if self.petEchidna == True:
                screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
        screen.blit(self.kangaroo1,((x_coord),(400*self.rat[1])))
        pygame.display.flip()
        p.pause(.5)
        if self.current_space > 40:
            words = text.Text(("Whoohoo! You finished! You made it to the end of time. ","Now you can sit back, relax, and watch the world burn.","","Press 'y' to play again, or 'enter' to quit the game."))
            words.usergiveinput()
            decision = words.choices()
            if decision == 'y':
                with open(r"etc\current_space.txt","w") as file:
                    file.write("0")
                while self.currentspace < 41:
                    self.spaces()
                    with open(r"etc\current_space.txt") as file:
                        self.currentspace = int(file.read())
            else:
                pygame.quit()
        else:
            words = text.Text(("You are now on space " + str(self.current_space), "","","Press 'enter' at any time to continue."))
        words.regulartext("True")
    def flop(self):
        num = (self.size[0]/24)
        x_coord = ((self.current_space_abs*num*4)-(100*self.rat[0]))
        count = 0
        spaces = abs(self.space)
        current_space = self.current_space
        while count < spaces:
            count += 1
            b = background.Background()
            self.bg = b.picture()
            self.reset = b.reset()
            location = b.shoplocation()
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                    screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo1,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.25)
            current_space = current_space - 1
            with open(r"etc\current_space.txt","w") as file:
                file.write(str(current_space))
            reset_screen = b.reset()
            if reset_screen == True:
                self.current_space_abs = self.currentspaceabsolute()
                if self.current_space_abs == 5:
                    b = background.Background()
                    self.bg = b.picture()
                    location = b.shoplocation()
                    x_coord = ((self.current_space_abs*num*4)+(100*self.rat[1]))
                    reset_screen = False
            else:
                x_coord -= num
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                    screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo3,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.25)
            x_coord -= num
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                    screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo4,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.25)
            x_coord -= num
            screen.blit(self.bg,(0,-23))
            screen.blit(self.shop, location)
            self.petEchidna = s.echidna()
            if self.petEchidna == True:
                    screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
            screen.blit(self.kangaroo5,((x_coord),(400*self.rat[1])))
            pygame.display.flip()
            p.pause(.25)
            x_coord -= num
            s.entershop()
        with open(r"etc\current_space.txt","w") as file:
            file.write(str(current_space))
        screen.blit(self.bg,(0,-23))
        screen.blit(self.shop, location)
        self.petEchidna = s.echidna()
        if self.petEchidna == True:
                screen.blit(self.echidna,(((x_coord*self.rat[0])-20*self.rat[0]),(600*self.rat[1])))
        screen.blit(self.kangaroo1,((x_coord),(400*self.rat[1])))
        pygame.display.flip()
        p.pause(.5)
        words = text.Text(("You are now on space " + str(current_space), "","","Press 'enter' at any time to continue."))
        words.regulartext("True")
