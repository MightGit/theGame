import pygame

class PlayerClass:

    xSpeed=0
    ySpeed=0
    maxSpeed=5

    color=(225 , 250 , 25)
    points=0
    collisionSFX = pygame.mixer.Sound('PopSound.mp3')
    DeathSFX = pygame.mixer.Sound('DieEffect.mp3')
    whatFish = 1


    def __init__(self,screen,xpos,ypos,terrainCollection):
        self.x=xpos
        self.y=ypos
        self.goldfishIMG20 = pygame.image.load('Goldfish20x20.png')
        self.goldfishIMG10 = pygame.image.load('Goldfish10x10.png')
        self.clownfishIMG20 = pygame.image.load('Clownfish20x20.png')
        self.clownfishIMG10 = pygame.image.load('Clownfish10x10.png')
        self.AxolotlIMG20 = pygame.image.load('Axoltl20x20.png')
        self.AxolotlIMG10 = pygame.image.load('Axoltl_10x10.png')


        self.goldfishSize = self.goldfishIMG20
        self.clownfishSize = self.clownfishIMG20
        self.AxolotlSize = self.AxolotlIMG20

        self.width = self.goldfishIMG20.get_size()[0]
        self.height = self.goldfishIMG20.get_size()[1]
        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]
        self.terrainCollection=terrainCollection



    def changeSpeedTo(self,newSpeed): #changes max speed, and takes current speeed into account
        self.maxSpeed += newSpeed
        if self.xSpeed > 0:
            self.xSpeed = self.maxSpeed
        elif self.xSpeed < 0:
            self.xSpeed = (-1)*self.maxSpeed
        if self.ySpeed > 0:
            self.ySpeed = self.maxSpeed
        elif self.ySpeed < 0:
            self.ySpeed = (-1)*self.maxSpeed
    def changeSpeedToFixed(self,newSpeed): #changes max speed, and takes current speeed into account
        self.maxSpeed = newSpeed
        if self.xSpeed > 0:
            self.xSpeed = self.maxSpeed
        elif self.xSpeed < 0:
            self.xSpeed = (-1)*self.maxSpeed
        if self.ySpeed > 0:
            self.ySpeed = self.maxSpeed
        elif self.ySpeed < 0:
            self.ySpeed = (-1)*self.maxSpeed

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

    def draw(self):
        rotationAngle = 0
        if self.ySpeed / self.maxSpeed * 180 > 0:
            rotationAngle += 180

        rotationAngle +=  (-self.xSpeed / self.maxSpeed * 90)
        if self.whatFish == 1:
            tempFish = pygame.transform.rotate(self.goldfishSize, rotationAngle)
        elif self.whatFish == 2:
            tempFish = pygame.transform.rotate(self.clownfishSize, rotationAngle)
        elif self.whatFish == 3:
            tempFish = pygame.transform.rotate(self.AxolotlSize, rotationAngle)
        else:
            tempFish = pygame.transform.rotate(self.goldfishSize, rotationAngle)

        self.theScreen.blit(tempFish,(self.x,self.y))
