import sys

import pygame

# TODO WSAD sterowanie


def check_events(ship):
    """Reakcja na zdarzenia generowane przez klawiature i myszkę"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship, character):
    """Uaktualnia obraz na ekranie i przejście do nowgo ekranu"""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    character.blitme()
    # Wyświetlnie ostanio modyfikowanego ekranu
    pygame.display.flip()
