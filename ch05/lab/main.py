import pygame
#This wasn't supposed to be uploaded with my midterm--I'm not sure why it uploaded this :( I'm not done yet
objs_in_seq = {}
def np1(n):
    global objs_in_seq
    num = n
    count = 0 
    while n > 1.0:
        count +=1
        if n % 2 == 0:
            n /= 2
        else:
            n = ((n*3)+1)
    objs_in_seq[num]=count
def np1range(x):
    for i in range(2,x):
        np1(i)
    print(objs_in_seq)
def draw(x):
    pygame.init()
    screen = pygame.display.set_mode()
    pygame.time.wait(500)
    new_display = pygame.transform.flip(screen, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    lines = pygame.draw.lines(new_display, "white", True, x,1)
    screen.blit(lines)
    pygame.display.flip()
    pygame.time.wait(500)
def main(): 
    x = int(input())
    np1range(x)
    tuples = list(objs_in_seq.items())
    print(tuples)
    draw(tuples)
main()
