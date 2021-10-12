import pygame
from pygame import image

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_to_rigth = False
        self.move_to_left = False

    def update(self):
        if self.move_to_rigth:
            self.rect.x += 1
        if self.move_to_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)