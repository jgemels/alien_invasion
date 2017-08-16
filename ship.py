import pygame


class Ship():
    """Klasa opisujaca statek gracza"""

    def __init__(self, screen):
        """Inicjalizacja statku kosmicznego i jego położenia początkowego"""
        self.screen = screen

        # Wczytywanie obrazu statku kosmiecznego i pobieranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Uaktualnienie położenia statku na podstawie opcji
        wskazującej na jego ruch
        """
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)
