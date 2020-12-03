import pygame


class ButtonMaker:
    color=(200 , 50, 50)

    def __init__(self,screen,x,y):
        self.theScreen=screen
        self.MenuButton = pygame.image.load('Play_Button.png')
        self.x=x
        self.y=y
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]

    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))


class Bagground:
    color = (200, 50, 50)

    def __init__(self, screen, x, y):
        self.theScreen = screen
        self.MenuButton = pygame.image.load('Baggrund_med_diverse.png')
        self.x = x
        self.y = y
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]

    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))
class GameBagground:
    color = (200, 50, 50)

    def __init__(self, screen, x, y):
        self.theScreen = screen
        self.MenuButton = pygame.image.load('Baggrund.png')
        self.x = x
        self.y = y
        self.width = self.MenuButton.get_size()[0]
        self.height = self.MenuButton.get_size()[1]

    def draw(self):
        self.theScreen.blit(self.MenuButton, (self.x, self.y))