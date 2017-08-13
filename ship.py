import pygame


class Ship():
    """Klasa opisujaca statek gracza"""

    def __init__(self, screen):
        """Inicjalizacja statku kosmicznego i jego położenia początkowego"""
        self.screen = screen

        # Wczytywanie obrazu statku kosmiecznego i poieranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get.react()
        self.screen_react = screen.get.react()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.centerx = self.screnn_rect.centerx
        self.rect.bottom = self.screnn_rect.bottom

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)
