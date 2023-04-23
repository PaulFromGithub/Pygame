import pygame
from pygame.sprite import Group

from settings import Settings
import funcions as func


def run():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Game")
    zombies = Group()

    while True:
        func.events(game_settings, screen)
        func.update_screen(game_settings, screen, zombies)
        func.create_zombie(game_settings, screen, zombies)


run()
