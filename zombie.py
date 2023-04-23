import pygame
from pygame.sprite import Sprite


class Zombie(Sprite):
    def __init__(self, game_settings, screen):
        super(Zombie, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("image/zombie_1.png")
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True