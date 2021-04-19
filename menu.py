import pygame
from pygame import freetype
from constants import *
from window_sizing import ScaleWindow, AspectWindow, TextWindow


def menu(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu Screen")

    # define Window elements
    window = AspectWindow(BLUE, (16, 9), (0.5, 0.5), 1)
    game_space = AspectWindow(GREEN, (1, 1), (4.5/16, 0.5), 0.9)
    start = TextWindow(RED, (16, 7), (0.5, 0.5), 0.3, "Start")
    info_space = AspectWindow(WHITE, (7, 9), (12.5/16, 0.5), 0.8)
    title = TextWindow(RED, (16, 5), (0.5, 0.2), 0.8, "Snake")

    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {'w': 500, 'h': 300}))
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
                start.resize(game_space.image)
                info_space.resize(window.image)
                title.resize(info_space.image)

            if event.type == pygame.MOUSEBUTTONUP:
                print(title.rect.collidepoint(pygame.mouse.get_pos()), pygame.mouse.get_pos(),title.image.get_rect(), title.rect)

                if title.rect.collidepoint(pygame.mouse.get_pos()):
                    print(2)

        # blit the child surface onto the parent surface, at a position relative to the parent
        screen.blit(window.image, (window.rect.x, window.rect.y))

        window.image.blit(game_space.image, (game_space.rect.x, game_space.rect.y))
        window.image.blit(info_space.image, (info_space.rect.x, info_space.rect.y))
        info_space.image.blit(title.image, (title.rect.x, title.rect.y))
        game_space.image.blit(start.image, (start.rect.x, start.rect.y))

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    pygame.freetype.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    menu(main_screen)
    pygame.quit()