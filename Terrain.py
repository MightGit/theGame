import pygame
from random import randint as rando

class TerrainClass:
    color=( 117, 119,117)

    def __init__(self,screen,_x,_y,_width,_height):
        self.theScreen=screen
        self.x=_x
        self.y=_y
        self.whatSkrald = rando(1,6)
        self.Terrain1 = pygame.image.load('Skrald_20X90.png')
        self.Terrain2 = pygame.image.load('Skrald_200X100.png')
        self.Terrain3 = pygame.image.load('Skrald_40X70.png')
        self.Terrain4 = pygame.image.load('Skrald_50X50.png')
        self.Terrain5 = pygame.image.load('Skrald_100X200.png')
        self.Terrain6 = pygame.image.load('Skrald_70X40.png')
        if self.whatSkrald ==1:
            self.width = self.Terrain1.get_size()[0]
            self.height = self.Terrain1.get_size()[1]
        if self.whatSkrald ==2:
            self.width = self.Terrain2.get_size()[0]
            self.height = self.Terrain2.get_size()[1]
        if self.whatSkrald ==3:
            self.width = self.Terrain3.get_size()[0]
            self.height = self.Terrain3.get_size()[1]
        if self.whatSkrald ==4:
            self.width = self.Terrain4.get_size()[0]
            self.height = self.Terrain4.get_size()[1]
        if self.whatSkrald ==5:
            self.width = self.Terrain5.get_size()[0]
            self.height = self.Terrain5.get_size()[1]
        if self.whatSkrald ==6:
            self.width = self.Terrain6.get_size()[0]
            self.height = self.Terrain6.get_size()[1]

    def draw(self):
        if self.whatSkrald ==1:
            self.theScreen.blit(self.Terrain1, (self.x, self.y))
        if self.whatSkrald ==2:
            self.theScreen.blit(self.Terrain2, (self.x, self.y))
        if self.whatSkrald ==3:
            self.theScreen.blit(self.Terrain3, (self.x, self.y))
        if self.whatSkrald ==4:
            self.theScreen.blit(self.Terrain4, (self.x, self.y))
        if self.whatSkrald ==5:
            self.theScreen.blit(self.Terrain5, (self.x, self.y))
        if self.whatSkrald ==6:
            self.theScreen.blit(self.Terrain6, (self.x, self.y))