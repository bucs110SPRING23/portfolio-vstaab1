import pygame
pygame.init()
window = pygame.display.set_mode()
class Ratio:
    def __init__(self):
        self.size = pygame.display.get_window_size()
        self.ratio = []
        self.ratio.append(int(self.size[0]/1536))
        self.ratio.append(int(self.size[1]/846))
    def fetchRatio(self):
        return self.ratio
    def fetchSize(self):
        return self.size