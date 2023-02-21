import turtle
import random
import time
import math
import pygame
window = turtle.getscreen
def pause(x):
    time.sleep(x)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
turtle.color("brown","green")
t1.goto(-100,-20)
t2.goto(-100,20)
t1move = int(random.randrange(1,101))
t2move = int(random.randrange(1,101))
pause(.5)
t1.forward(t1move)
t2.forward(t2move)
pause(.5)
t1.goto(-100,-20)
t2.goto(-100,20)
pause(.5)


for i in range(10):
    t1move = int(random.randrange(1,11))
    t2move = int(random.randrange(1,11))
    t1.forward(t1move)
    t2.forward(t2move)
    pause(.5)
t1.goto(-100,-20)
t2.goto(-100,20)
turtle.exitonclick()

pygame.init()
window = pygame.display.set_mode()
points = []
num_sides = [3,4,6,20,100,360]
side_length = 25
x = 0
y = 0
for i in range(num_sides[0]):
    print(i)
    xpos = 10
    ypos = 10
    angle = 360/num_sides[0]
    radians = math.radians(angle * i)
    x += xpos + (side_length * math.cos(radians))
    y += ypos + (side_length * math.sin(radians))
    points.append((x,y))
    print(points)
    print(type(points[i-1]))
    if i == num_sides[0]:
        pygame.draw.polygon(window,"red",(points),0)
        num_sides.remove[0]