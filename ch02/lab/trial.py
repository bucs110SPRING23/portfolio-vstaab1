import math
import pygame

pygame.init()
window = pygame.display.set_mode((800,600))
points = []
num_sides = [3,4,6,20,100,360]
side_length = 200
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
game = True

def run():
    pygame.display.flip()
    x = 0
    y = 0   
    z = 0
    xpos = 400
    ypos = 300
    global points
    global num_sides
    while z < num_sides[0]:
        angle = 360/num_sides[0]
        radians = math.radians(angle * z)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append((x,y))
        z += 1
    if z == num_sides[0]:
        pygame.display.flip()
        window.fill(white)
        pygame.draw.polygon(window,red,(points),1)
        pygame.time.wait(1000)
        num_sides.remove(num_sides[0])
        points.clear()
        pygame.display.flip()
        z = 0
        if 360 in num_sides:
            run()
        else:
            pygame.quit()
            quit()
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    run()


