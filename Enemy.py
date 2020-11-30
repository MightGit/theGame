import pygame
from random import randint as rando



class EnemyClass:
    xSpeed=0
    ySpeed=0
    maxSpeed=5

    color=( 35, 53, 97)
    points=0
    enemyTime = 0



    def __init__(self,screen,terrainCollection,player):
        self.playerObject=player
        self.theScreen=screen

        self.Shark30 = pygame.image.load('Shark_1_30x30.png')
        self.width = self.Shark30.get_size()[0]
        self.height = self.Shark30.get_size()[1]
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]
        self.terrainCollection=terrainCollection
        self.randomLocation = rando(1,4)
        if self.randomLocation == 1:
            self.x = 0
            self.y = 0
        if self.randomLocation == 2:
            self.x = 1180
            self.y = 780
        if self.randomLocation == 3:
            self.x = 1180
            self.y = 0
        if self.randomLocation == 4:
            self.x = 0
            self.y = 780

    def enemyDeadTimer(self):
        self.enemyTime +=1

    def update(self):


        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed

        xWillCollide = False
        yWillCollide = False

        for tile in self.terrainCollection:
            #if the player is within the x coordinates of a wall tile, and future Y coordinate is inside the wall:
            if self.x + self.width > tile.x and self.x < tile.x + tile.width and self.futureY + self.height > tile.y and self.futureY < tile.y + tile.height:
                yWillCollide=True
            # if the player is within the Y coordinates of a wall tile, and future X coordinate is inside the wall:
            if self.y + self.height > tile.y and self.y < tile.y + tile.height and self.futureX + self.width > tile.x and self.futureX < tile.x + tile.width:
                xWillCollide=True

        if not xWillCollide:
            self.x = self.futureX
        if not yWillCollide:
            self.y = self.futureY

        #safety to prevent overshoot:
        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        #from main import playerObject


        if self.x < self.playerObject.x:
            self.xSpeed = 1
        if self.y < self.playerObject.y:
            self.ySpeed = 1

        if self.x > self.playerObject.x:
            self.xSpeed =- 1
        if self.y > self.playerObject.y:
            self.ySpeed =- 1



    def draw(self):
        self.theScreen.blit(self.Shark30, (self.x, self.y))