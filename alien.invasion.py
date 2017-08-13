import sys

import pygame


from settings import Settings
from ship import Ship


def run_game():
    # Inicializacja gry i utowrzenie obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie statku kosmicznego
    ship = Ship(screen)

    # Rozpoczęcie pętli głównej gry
    while True:

        # Oczekiwnaie na naciśnięcie klaiwsza lub przycisk myszy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Odświeżenie ekranu w trakcie każdej iteracji pętli
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Wyświetlnie ostanio modyfikowanego ekranu
        pygame.display.flip()


run_game()
