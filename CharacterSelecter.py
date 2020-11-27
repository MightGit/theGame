import pygame


class Goldfish:
    color=(225 , 250 , 25)

    def __init__(self,screen,x,y,width,height):
        self.theScreen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class ClownFish:
    color=(200 , 50, 250)

    def __init__(self,screen,x,y,width,height):
        self.theScreen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
class Axolotl:
    color=(250 , 20, 50)

    def __init__(self,screen,x,y,width,height):
        self.theScreen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
