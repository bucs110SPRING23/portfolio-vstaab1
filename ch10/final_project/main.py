import pygame
from src import startwindow
# import your controller


def main():
    pygame.init()
    window = pygame.display.set_mode()
    s = startwindow.Start()
    s.start()
    # Create an instance on your controller object
    # Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
#if __name__ == "__main__":
main()
