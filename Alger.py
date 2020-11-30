import pygame
from random import randint as rando

class AlgerClass:
    color = ( 13 , 101 , 34)

    def __init__(self, screen, _x, _y, _width, _height):
        self.theScreen = screen
        self.x = _x
        self.y = _y
        self.whatSkrald = rando(1,3)
        self.Terrain1 = pygame.image.load('Alge_20X40.png')
        self.Terrain2 = pygame.image.load('Alge_60X60.png')
        self.Terrain3 = pygame.image.load('Alge_80X40.png')

        if self.whatSkrald ==1:
            self.width = self.Terrain1.get_size()[0]
            self.height = self.Terrain1.get_size()[1]
        if self.whatSkrald ==2:
            self.width = self.Terrain2.get_size()[0]
            self.height = self.Terrain2.get_size()[1]
        if self.whatSkrald ==3:
            self.width = self.Terrain3.get_size()[0]
            self.height = self.Terrain3.get_size()[1]


    def draw(self):
        if self.whatSkrald == 1:
            self.theScreen.blit(self.Terrain1, (self.x, self.y))
        if self.whatSkrald == 2:
            self.theScreen.blit(self.Terrain2, (self.x, self.y))
        if self.whatSkrald == 3:
            self.theScreen.blit(self.Terrain3, (self.x, self.y))
