import pygame


class BottonMaker:
    color=(200 , 50, 50)

    def __init__(self,screen,x,y,width,height):
        self.theScreen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
