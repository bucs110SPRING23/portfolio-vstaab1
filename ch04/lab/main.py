import pygame
import random
import math
pygame.init()
q = 0
score = [0,0]
screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
player = ("yellow","white")
choice = ""
game = False
if size[0] > size[1]:
    radius = size[1]/2
else:
    radius = size[0]/2
center = []
center.append(size[0]/2)
center.append(size[1]/2)
start = False
def throw(z):
    global score
    x = random.randrange(0,size[0])
    y = random.randrange(0,size[1])
    distance_from_center = math.hypot((x-center[0]),(y-center[1]))
    if distance_from_center > radius:
        score[z] += 0
    else:
        score[z] += 1
    pygame.draw.circle(screen,player[z],(x,y),10,0)
    pygame.display.flip()
    pygame.time.wait(800)
def win(y):
    font = pygame.font.SysFont(None, (60))
    text = font.render(y, True, "red")
    screen.blit(text,(0,0))
    pygame.display.flip()
def play():
    global q
    while q < 10:
        throw(0)
        throw(1)
        q += 1
    if score[0]>score[1]:
        a = "Yellow player wins. Score: " + str(score[0])
        if choice == "yellow":
            b = "Congrats, you bet on the winning team!"
        else:
            b = "Aw, your team didn't win this time!"
    elif score[1]>score[0]:
        a = "White player wins. Score: " + str(score[1])
        if choice == "white":
            b = "Congrats, you bet on the winning team!"
        else:
            b = "Aw, your team didn't win this time!"
    else:
        a = "It's a tie! Score: " + str(score[0])
        b = "Oh well, better luck next time!"
    win(a)
    pygame.time.wait(2000)
    screen.fill("black")  
    win(b)
    pygame.time.wait(2000)
    pygame.quit()
def main():
    screen.fill("black")   
    pygame.draw.circle(screen,"purple",(center[0],center[1]),radius,0)
    play()
pygame.draw.rect(screen,"red",pygame.Rect(30,500,200,100))
pygame.draw.rect(screen,"red",pygame.Rect(250,500,200,100))
pygame.display.flip()
run = True
while run == True:
    x, y = pygame.mouse.get_pos()
    for event in pygame. event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if y >= 500:
            if y <= 600:
                if x >= 250: 
                    if x <= 450:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            choice = "white"
                            run = False
                            game = True
                            main() 
                elif x >= 30:
                    if x <= 230:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            choice = "yellow"
                            run = False
                            game = True
                            main()
        else:
            win("Click the left rectangle to bet on yellow or the right one to bet on white.")