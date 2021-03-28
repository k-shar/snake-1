import pygame
from pygame import freetype
import menu
import game

if __name__ == "__main__":
    # init the screen for the program
    pygame.display.init()
    pygame.freetype.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)

    # when menu is done it will return the state of the screen
    main_screen = menu.menu(main_screen)

    main_screen = game.game(main_screen)

    pygame.quit()
