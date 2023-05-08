import pygame
from src import ratio
class Screen:
    def __init__(self):
        with open(r"etc\KangaCash.txt") as file:
            self.KangaCash = file.read()
        pygame.init()
        self.screen = pygame.display.set_mode()
        r = ratio.Ratio()
        self.ratio = r.fetchRatio()
        self.font = pygame.font.SysFont(None, (60*self.ratio[1]))
        self.default_screen = [250, 204, 125]
        self.default_info = (("KangaCash Balance: ") + str(self.KangaCash))
        self.words = self.font.render(self.default_info, True, "Black")
    def display(self):
        pygame.init()
        self.screen.fill(self.default_screen)
        self.screen.blit(self.words,((1020*self.ratio[0]),(820*self.ratio[1])))