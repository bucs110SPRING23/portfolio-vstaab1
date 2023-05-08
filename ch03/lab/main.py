import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
print(size[0])
if size[0] > size[1]:
    radius = size[1]/2
else:
    radius = size[0]/2
center = []
center.append(size[0]/2)
center.append(size[1]/2)
pygame.draw.circle(screen,"purple",(center[0],center[1]),radius,0)
for i in range(10):
    x = random.randrange(0,size[0])
    y = random.randrange(0,size[1])
    distance_from_center = math.hypot((x-center[0]),(y-center[1]))
    if distance_from_center > radius:
        pygame.draw.circle(screen,"red",(x,y),10,0)
    else:
        pygame.draw.circle(screen,"green",(x,y),10,0)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)
pygame.quit()