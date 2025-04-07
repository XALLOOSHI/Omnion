import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.screen = pygame.display.set_mode((Width,Height))
        pygame.display.set_caption('Omnion')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.font_name = '8-BIT WONDER.TTF'
        self.WHITE = (0,0,0)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
         self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.screen.fill('black')
            self.draw_text('Omnion', 20, Width/2, Height/2 )
            self.screen.blit(self.screen, (0,0))
            self.reset_keys() 

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
            
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(Fps)
    
    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface,text_rect)


if __name__ == '__main__':
    game = Game()
    game.run()