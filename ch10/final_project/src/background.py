import pygame
from src import ratio
class Background:
    def __init__(self):
        r = ratio.Ratio()
        size = r.fetchSize()
        rat = r.fetchRatio()
        with open(r"etc\current_space.txt") as file:
            current_space = int(file.read())
        background1 = pygame.image.load(r'assets\background1.jpg').convert_alpha()
        background2 = pygame.image.load(r'assets\background2.jpg').convert_alpha()
        background3 = pygame.image.load(r'assets\background3.jpg').convert_alpha()
        background4 = pygame.image.load(r'assets\background4.jpg').convert_alpha()
        background5 = pygame.image.load(r'assets\background5.jpg').convert_alpha()
        background6 = pygame.image.load(r'assets\background6.jpg').convert_alpha()
        background7 = pygame.image.load(r'assets\background7.jpg').convert_alpha()
        num = (size[0]/12)
        if current_space <= 5:
            self.current_space_abs = current_space
            self.background = background1
            self.location = (-500*rat[0], -500*rat[1])
        elif current_space <= 11:
            self.current_space_abs = current_space - 6
            self.background = background2
            self.location = (num,200*rat[1])
        elif current_space <= 17:
            self.current_space_abs = current_space - 12
            self.background = background3
            self.location = (num*5,200*rat[1])
        elif current_space <= 23:
            self.current_space_abs = current_space - 18
            self.background = background4
            self.location = (-500*rat[0],-500*rat[1])
        elif current_space <= 29:
            self.current_space_abs = current_space - 24
            self.background = background5
            self.location = (num*5,200*rat[1])
        elif current_space <= 35:
            self.current_space_abs = current_space - 30
            self.background = background6
            self.location = (num*3,200*rat[1])
        else:
            self.current_space_abs = current_space - 36
            self.background = background7
            self.location = (-500*rat[0],-500*rat[1])
        if self.current_space_abs == 0:
            self.reset_screen = True
        elif self.current_space_abs == 5:
            self.reset_screen = True
        else:
            self.reset_screen = False
        self.background = pygame.transform.scale(self.background, (1536*rat[0],846*rat[1]))
    def picture(self):
        return self.background
    def shoplocation(self):
        return self.location
    def reset(self):
        return self.reset_screen