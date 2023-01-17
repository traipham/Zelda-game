import pygame
from settings import * 
import pygame.camera
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)

        self.image = pygame.image.load('./graphics/kiet_character.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos) # Rectangle always follow hitbox
        self.hitbox = self.rect.inflate(0, -self.rect.size[1]//3) # allows for overlapping of spirtes

        self.direction = pygame.math.Vector2() # x pos and y pos (0,0)
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        """Applies movement speed to key"""
        # If vector has any kind of length (vector of 0 can not be normalize)
        # This essentially helps moving diagonal at a normalized speed
        if self.direction.magnitude() != 0: 
            self.direction = self.direction.normalize() # set length of vector to 1 
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal') # Check if there is collision after moving horizontally
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical') # Check collision after movement 
        self.rect.center = self.hitbox.center
    

    def collision(self, direction):
        """Check for colision in the horizontal and vertical direction"""
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                # Check rectangle of sprite to rectangle of the player
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left 
                    elif self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                # Check rectangle of sprite to rectangle of the player
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top # get position of 
                    elif self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)

