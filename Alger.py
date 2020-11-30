import pygame


class AlgerClass:
    color = ( 13 , 101 , 34)

    def __init__(self, screen, _x, _y, _width, _height):
        self.theScreen = screen
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
