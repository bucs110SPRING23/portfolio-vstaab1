import pygame
from src import text
class Username:
    def __init__(self):
        self.end = "False"
        self.name = ""
    def takename(self):
        while self.end == "False":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.letter = 'A'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_b:
                        self.letter = 'B'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")                    
                    elif event.key == pygame.K_c:
                        self.letter = 'C'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_d:
                        self.letter = 'D'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_e:
                        self.letter = 'E'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_f:
                        self.letter = 'F'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_g:
                        self.letter = 'G'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_h:
                        self.letter = 'H'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_i:
                        self.letter = 'I'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_j:
                        self.letter = 'J'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_k:
                        self.letter = 'K'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_l:
                        self.letter = 'L'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_m:
                        self.letter = 'M'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_n:
                        self.letter = 'N'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_o:
                        self.letter = 'O'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_p:
                        self.letter = 'P'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_q:
                        self.letter = 'Q'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_r:
                        self.letter = 'R'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_s:
                        self.letter = 'S'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_t:
                        self.letter = 'T'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_u:
                        self.letter = 'U'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_v:
                        self.letter = 'V'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_w:
                        self.letter = 'W'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_x:
                        self.letter = 'X'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_y:
                        self.letter = 'Y'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_z:
                        self.letter = 'Z'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_SPACE:
                        self.letter = ' '
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_MINUS:
                        self.letter = '-'
                        self.name = str(self.name) + str(self.letter)
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.name) >= 1:
                            self.name = self.name[:-1]
                            words = text.Text((self.name,"","",""))
                            words.regulartext("False")
                        else:
                            self.name = self.name
                            words = text.Text((self.name,"","",""))
                            words.regulartext("False")
                    elif event.key == pygame.K_RETURN:
                        self.end = "True"
                        words = text.Text((self.name,"","",""))
                        words.regulartext("False")
        if self.end == "True":
            pygame.display.flip()
    def username(self):
        return self.name