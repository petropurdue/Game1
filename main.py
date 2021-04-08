import pygame, time
from pygame.locals import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pygame Keyboard Test')
    pygame.mouse.set_visible(0)
    while True:
        for event in pygame.event.get():

            if (event.type == KEYUP) or (event.type == KEYDOWN):
                print("keypress")
                time.sleep(0.1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
