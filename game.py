import pygame
from pygame import freetype
from constants import *
from window_sizing import AspectWindow, TextWindow

#######
def game(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game Screen")

    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {'w': screen.get_width(), 'h': screen.get_height()}))
    # define Window elements
    window = AspectWindow(BLUE, (16, 9), (0.5, 0.5), 1)
    game_space = AspectWindow(GREEN, (1, 1), (4.5/16, 0.5), 0.9)
    info_space = AspectWindow(WHITE, (7, 9), (12.5/16, 0.5), 0.8)
    title = TextWindow(RED, (16, 5), (0.5, 0.2), 0.8, "Title")

    while True:
        screen.fill(RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return screen
            if event.type == pygame.VIDEORESIZE:

                # resize largest to smallest, as to pass in the new resized parent surf
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                window.resize(screen)
                game_space.resize(window.image)
                info_space.resize(window.image)
                title.resize(info_space.image)

        # blit the child surface onto the parent surface, at a position relative to the parent
        screen.blit(window.image, (window.rect.x, window.rect.y))

        window.image.blit(game_space.image, (game_space.rect.x, game_space.rect.y))
        window.image.blit(info_space.image, (info_space.rect.x, info_space.rect.y))
        info_space.image.blit(title.image, (title.rect.x, title.rect.y))

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    pygame.freetype.init()
    game_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    game(game_screen)
    pygame.quit()
