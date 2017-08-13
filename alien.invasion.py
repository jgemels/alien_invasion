import pygame


from settings import Settings
from ship import Ship
import game_functions as gf


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
        gf.check_events()

        # Odświeżenie ekranu w trakcie każdej iteracji pętli
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Wyświetlnie ostanio modyfikowanego ekranu
        pygame.display.flip()


run_game()
