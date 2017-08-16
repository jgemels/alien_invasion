import pygame


class Character():
    """Klasa opisująca postać"""

    def __init__(self, screen):
        """Inicjalizacja postaci i jej połozenia początkowego"""
        self.screen = screen

        # Wczytywanie obrazu postaci i pobieranie jej prostokąta
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowa postać pojawia się na środku ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Wyświetlanie postaci w jej aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)
