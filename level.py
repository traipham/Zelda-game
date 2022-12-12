# Needs to be able to manage many sprites (Mobs, character)
# Visible_sprites = only spirtes with will draw
# Obstacl_sprites = group of sprites that the player can collide with 

import pygame

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface() # get the window surface


        # visible sprite group
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()

    def run(self):
        # update and draw the game 
        pass
