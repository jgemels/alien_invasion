import sys

import pygame


def check_events():
    """Reakcja na zdarzenia generowane przez klawiature i myszkę"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
