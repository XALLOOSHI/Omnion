import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width,Height))
        pygame.display.set_caption('Omnion')
        self.clock = pygame.time.Clock()
        self.level = Level()


def run(self):
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        self.screen.fill('black')
        self.level.run()
        pygame.display.updated()
        self.clock.tick(Fps)

if __name__ == '__main__':
    game = Game()
    game.run()