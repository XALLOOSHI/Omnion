import pygame

class Level:
    def __init__(self):
        #Display surface
        self.display_surface = pygame.display.get_surface()
        #Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        pass