import pygame, sys
import random

from level import Level

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_BG_COLOR = (250, 234, 203)
GAME_TITLE = "Zelda RPG"
class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption(GAME_TITLE)
        # icon = pygame.image.load('game_icon\\window_icon.png') # TODO: game icon
        # pygame.display.set_icon(icon) # TODO: game icon
    def run(self):
        while True:
            self.window.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)



if __name__ == "__main__":
    game = Game()
    game.run()