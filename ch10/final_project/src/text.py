import pygame
from src import pause
from src import screen
from src import ratio
pygame.init()
p = pause.Pause()
r = ratio.Ratio()
rat = r.fetchRatio()
font = pygame.font.SysFont(None, (60*rat[1]))
class Text:
    def __init__(self, words):
        self.enter = True
        self.posx = 10*rat[0]
        self.posy = 10*rat[1]
        self.position = self.posx, self.posy
        self.p, self.q, self.r, self.s = words
        self.screen = pygame.display.set_mode()
        self.text1 = font.render(self.p, True, "Black")
        self.text2 = font.render(self.q, True, "Black")
        self.text3 = font.render(self.r, True, "Black")
        self.text4 = font.render(self.s, True, "Black")
    def usergiveinput(self):
        s = screen.Screen()
        s.display()
        self.screen.blit(self.text1,(self.position[0],(int(self.position[1])+int(75*int(0)))))
        self.screen.blit(self.text2,(self.position[0],(int(self.position[1])+int(75*int(1)))))
        self.screen.blit(self.text3,(self.position[0],(int(self.position[1])+int(75*int(2)))))
        self.screen.blit(self.text4,(self.position[0],(int(self.position[1])+int(75*int(3)))))
        pygame.display.flip()
        p.pause(.1)
        end = False
        while end == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.choice = 'y'
                        end = True
                    elif event.key == pygame.K_n:
                        self.choice = 'n'
                        end = True
                    elif event.key == pygame.K_a:
                        self.choice = 'a'
                        end = True
                    elif event.key == pygame.K_b:
                        self.choice = 'b'
                        end = True
                    elif event.key == pygame.K_c:
                        self.choice = 'c'
                        end = True
                    elif event.key == pygame.K_RETURN:
                        self.choice = ' '
                        end = True
    def regulartext(self,enter):
        if enter == "True":
            while enter == "True":
                s = screen.Screen()
                s.display()
                self.screen.blit(self.text1,(self.position[0],(int(self.position[1])+int(75*int(0)))))
                self.screen.blit(self.text2,(self.position[0],(int(self.position[1])+int(75*int(1)))))
                self.screen.blit(self.text3,(self.position[0],(int(self.position[1])+int(75*int(2)))))
                self.screen.blit(self.text4,(self.position[0],(int(self.position[1])+int(75*int(3)))))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.choice = ' '
                            enter = "False"
                            pygame.display.flip()
                            p.pause(.2)
        else:
            s = screen.Screen()
            s.display()
            self.screen.blit(self.text1,(self.position[0],(int(self.position[1])+int(75*int(0)))))
            self.screen.blit(self.text2,(self.position[0],(int(self.position[1])+int(75*int(1)))))
            self.screen.blit(self.text3,(self.position[0],(int(self.position[1])+int(75*int(2)))))
            self.screen.blit(self.text4,(self.position[0],(int(self.position[1])+int(75*int(3)))))
            pygame.display.flip()
    def choices(self):
        return self.choice
    def numericalinput(self):
        s = screen.Screen()
        s.display()
        self.screen.blit(self.text1,(self.position[0],(int(self.position[1])+int(75*int(0)))))
        self.screen.blit(self.text2,(self.position[0],(int(self.position[1])+int(75*int(1)))))
        self.screen.blit(self.text3,(self.position[0],(int(self.position[1])+int(75*int(2)))))
        self.screen.blit(self.text4,(self.position[0],(int(self.position[1])+int(75*int(3)))))
        pygame.display.flip()
        p.pause(.1)
        for event in pygame.event.get():
            end = False
            self.choice = ""
            while end == False:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.number = '1'
                            self.choice = str(self.choice) + str(self.number)
                            end = True
                        elif event.key == pygame.K_2:
                            self.number = '2'
                            self.choice = str(self.choice) + str(self.number)
                            end = True
                        elif event.key == pygame.K_3:
                            self.number = '3'
                            self.choice = str(self.choice) + str(self.number)
                            end = True
                        elif event.key == pygame.K_4:
                            self.number = '4'
                            self.choice = str(self.choice) + str(self.number)
                            end = True
                        elif event.key == pygame.K_MINUS:
                            self.number = '-'
                            self.choice = str(self.choice) + str(self.number)
                            end = False
                        elif event.key == pygame.K_BACKSPACE:
                            if len(self.choice) >= 1:
                                self.choice = self.choice[:-1]
                                end = False
                            else:
                                self.choice = self.choice
                                end = False
    def numericaloutput(self):
        return self.choice