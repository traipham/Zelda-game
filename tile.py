import pygame
from settings import * 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        orig_image = pygame.image.load('./graphics/rock.png').convert_alpha()
        self.image = pygame.transform.scale(orig_image, (64,64))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10) # Changes the size of rectangle (same width and center, but top and bottom is a smaller size (shrink by 5 top and bottom))