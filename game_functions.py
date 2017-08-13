import sys

import pygame


def check_events():
    """Reakcja na zdarzenia generowane przez klawiature i myszkę"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Uaktualnia obraz na ekranie i przejście do nowgo ekranu"""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    ship.blitme(ai_settings, screen, ship)

    # Wyświetlnie ostanio modyfikowanego ekranu
    pygame.display.flip()
