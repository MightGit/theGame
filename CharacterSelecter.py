import pygame


class Goldfish:
    color=(225 , 250 , 25)

    def __init__(self,screen,x,y):
        self.MenuButton = pygame.image.load('BIllede_af_klovnfisk.png')
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]
        self.theScreen=screen
        self.x=x
        self.y=y


    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))

class ClownFish:
    color=(255, 126, 0)

    def __init__(self,screen,x,y):
        self.MenuButton = pygame.image.load('Guldfisken_125x50.png')
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]
        self.theScreen=screen
        self.x=x
        self.y=y


    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))

class Axolotl:
    color=(255, 237, 253)

    def __init__(self,screen,x,y):
        self.MenuButton = pygame.image.load('BIllede_af_axolotl.png')
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]
        self.theScreen=screen
        self.x=x
        self.y=y


    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))