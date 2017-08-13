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
        gf.update_screen(ai_settings, screen, ship)


run_game()
