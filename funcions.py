import pygame
import sys
from zombie import Zombie


def update_screen(game_settings, screen, zombies):
    screen_image = pygame.image.load(game_settings.bg_image).convert()
    screen.blit(screen_image, [0, 0])
    zombies.draw(screen)
    pygame.display.flip()


def events(game_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


def create_zombie(game_settings, screen, zombies):
    zombie = Zombie(game_settings, screen)
    zombies.add(zombie)