#/usr/bin/python
import pygame
from sys import exit as sys_exit
import settings


class BugTheGame:
    def __init__(self):
        pygame.init()
        self.settings = settings

        self.screen = pygame.display.set_mode((self.settings.WIDTH,self.settings.HEIGHT))

        self.background_img = pygame.image.load(self.settings.bg_image)
        self.bg_rect = self.background_img.get_rect()
        self.bg_rect.center = (200,200)

        pygame.display.set_caption("BUG THE GAME")
        

    def run_game(self):

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys_exit()


            self.screen.fill(self.settings.bg_color)            
            self.screen.blit(self.background_img, (0,0))
            pygame.display.flip()


if __name__ != '__init__':
    BTG = BugTheGame()