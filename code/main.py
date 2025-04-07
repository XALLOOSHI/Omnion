import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.screen = pygame.display.set_mode((Width,Height))
        self.display = pygame.Surface((Width,Height))
        pygame.display.set_caption('Omnion')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.font_name = None
        self.WHITE = (255,255,255)
        self.menu_options = ["Start Game", "Quit"]
        self.selected_option = 0

    def main_menu(self):
        while self.running:
            self.check_events()

            # Navigate menu
            if self.DOWN_KEY:
                self.selected_option = (self.selected_option + 1) % len(self.menu_options)
            elif self.UP_KEY:
                self.selected_option = (self.selected_option - 1) % len(self.menu_options)
            elif self.START_KEY:
                if self.selected_option == 0:  # Start Game
                    self.playing = True
                    self.game_loop()
            elif self.selected_option == 1:  # Quit
                pygame.quit()
                sys.exit()

        # Drawing menu (NOW INSIDE THE LOOP)
            self.display.fill((0, 0, 0))
            for i, option in enumerate(self.menu_options):
                color = (255, 255, 0) if i == self.selected_option else self.WHITE
                self.draw_text(option, 40, Width / 2, Height / 2 + i * 50, color)

            print("Rendering menu frame...")  # This will print every frame

            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(Fps)
            self.reset_keys()

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
            self.display.fill('black')
            self.draw_text('Omnion', 20, Width/2, Height/2)
            self.screen.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys() 

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
            
            self.screen.fill('black')
            self.screen.blit(self.display, (0,0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(Fps)
    
    def draw_text(self, text, size, x,y, color ):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


if __name__ == '__main__':
    game = Game()
    game.main_menu()
    #game.playing = True 
    #game.game_loop()
    #game.run()