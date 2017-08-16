import pygame


from settings import Settings
from ship import Ship
from character import Character
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
    # Utworzenie postaci
    character = Character(screen)

    # Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, character)


run_game()
