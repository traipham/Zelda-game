# Needs to be able to manage many sprites (Mobs, character)
# Visible_sprites = only spirtes with will draw
# Obstacl_sprites = group of sprites that the player can collide with 
import pygame
from settings import *

from tile import Tile
from player import Player
from test.debug import *
class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface() # get the window surface

        # visible sprite group
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # map setup
        self.create_map()

    def create_map(self):
        """Create map based on map from settings.py, p = player, x = obstacles
            Initialize the obstacles and player
        """
        for row_ind, row in enumerate(WORLD_MAP):
            for col_ind, col in enumerate(row):
                x_pos = row_ind * TILESIZE
                y_pos = col_ind * TILESIZE
                if col == 'x':
                    Tile((x_pos, y_pos), [self.visible_sprites, self.obstacle_sprites])
                    pass
                if col == 'p':
                    self.player = Player((x_pos, y_pos), [self.visible_sprites], self.obstacle_sprites)       

    def run(self):
        # update and draw the game 
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.rect)
        # debug(self.player.direction)
        pass

class YSortCameraGroup(pygame.sprite.Group):
    """Camera for sprite sorted by Y coordinates"""
    def __init__(self):
        super().__init__()
        # general setup
        self.display_surface = pygame.display.get_surface() # get current surface
        self.half_width = self.display_surface.get_size()[0] // 2 # Get half size_x of screen
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(0,0) # Used as camera 

    def custom_draw(self, player):
        """Camera movement when player is moving and drawing obstacles and players"""
        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width # Center offset
        self.offset.y = player.rect.centery - self.half_height

        # This is what the normal sprite.group.draw() is doing
        # for sprite in self.sprites():
        #     offset_pos = sprite.rect.topleft - self.offset # Center position to character (camera have to move out of map)
        #     self.display_surface.blit(sprite.image, offset_pos) # Constaly draw image based on character position

        # Sort the sprite by y position so that if player's y pos is < than obstacle player will go overlap obstacle
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset # Center position to character (camera have to move out of map)
            self.display_surface.blit(sprite.image, offset_pos) # Constaly draw image based on character position
