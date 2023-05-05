import pygame
pygame.init()
class Pause:
    def __init__(self):
        self.time = 1000
    def pause(self,num):
        time = int(self.time*num)
        pygame.time.wait(time)