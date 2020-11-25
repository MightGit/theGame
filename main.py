import pygame
#testtesttest123
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.mixer.music.load('Flowers for Bodysnatchers - Hearken Our Storm.mp3') #https://soundcloud.com/synthwave80s/01-vice-point
pygame.mixer.music.play(-1)

from Player import PlayerClass
from Enemy import EnemyClass
from Terrain import TerrainClass
from Alger import AlgerClass

from random import randint as rando
clock = pygame.time.Clock()

gameWindowHeight=800
gameWindowWidth=1200
movementPower = 0

terrain=[]
enemies=[]

algers=[]

highScore=0

powerup=0

tideDecider = 0
tideX = 0.0
tideY = 0.0
try:
    with open('highScoreFile') as file:
        data = file.read()
        highScore=int(data.strip())
        print("Loaded highscore:",highScore)
except:
    print("highScoreFile not found, resetting to 0.")

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))


def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True

def spawnEnemy():
    enemies.append(EnemyClass(screen,xpos=rando(0,gameWindowWidth),ypos=rando(0,gameWindowHeight),terrainCollection=terrain))


for i in range(10):
    spawnEnemy()

def createTerrain():
    terrain.append(TerrainClass(screen, rando(-200,gameWindowWidth + 200),rando(-200,gameWindowHeight + 200),rando(10,100),rando(10,100)))


def createAlger():
    algers.append(AlgerClass(screen, _x= rando(-100,gameWindowWidth+100), _y=rando(-100,gameWindowHeight+100),_width=rando(20,75) ,_height=rando(20,75)))

for i in range(6):
    createAlger()

for i in range(15):
    createTerrain()


playerObject = PlayerClass(screen,xpos=100, ypos=100,terrainCollection=terrain)


done = False
while not done:

#    print(tideDecider)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        #-------PLAYER CONTROLS---------

        #KEY PRESSES:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject.xSpeed -= playerObject.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject.xSpeed += playerObject.maxSpeed
                #Skud:                          .. Men kun når spilleren bevæger sig:

        #KEY RELEASES:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject.xSpeed += playerObject.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject.xSpeed -= playerObject.maxSpeed
    #debug: print out unused pygame events
    #else:
    #        print(event)

    #UPDATE GAME OBJECTS:

    playerObject.update()


    for enemy in enemies:
        enemyIsDead = False #boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()

        if enemy.x>gameWindowWidth or enemy.y>gameWindowHeight or enemy.x<0 or enemy.y<0:
            enemyIsDead=True

        for alger in algers:
            if collisionChecker(alger,playerObject):
                algers.remove(alger)
                playerObject.collisionSFX.play()
                playerObject.points +=1
                createAlger()
                spawnEnemy()

                powerup = rando(0, 30)
                if powerup == 14:
                    playerObject.height+=10
                    playerObject.width+=10

                #print('Points:',playerObject.points)
                if playerObject.points > highScore:
                    highScore = playerObject.points
        if collisionChecker(enemy,playerObject):
            playerObject.DeathSFX.play()
            print("OUCH!")
            playerObject.points = 0



        if enemyIsDead:
            enemies.remove(enemy)
            spawnEnemy()

        if tideDecider % 400 == 0:
            tideX = rando(-1,1)
            tideY = rando(-1,1)

    if tideDecider % 3 == 0:
        for alger in algers:
            alger.x = alger.x - tideX
            alger.y = alger.y - tideY
        for tile in terrain:
            tile.x = tile.x - tideX
            tile.y = tile.y - tideY
    if tideDecider % 200 == 0:
        createAlger()
        createTerrain()

    if playerObject.points==30 and movementPower == 0:
        playerObject.height= 10
        playerObject.width= 10
        movementPower = 1


    #DRAW GAME OBJECTS:
    screen.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
    playerObject.draw()

    #Score:                                                 antialias?, color
    text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
    screen.blit(text,(0,0))

    text = font.render('HIGHSCORE: ' + str(highScore), True, (255, 0, 0))
    screen.blit(text, (300,0))


    for enemy in enemies:
        enemy.draw()

    for tile in terrain:
        tile.draw()
    for alger in algers:
        alger.draw()



    pygame.display.flip()
    clock.tick(60)
    tideDecider = tideDecider + 1

#When done is false the while loop above exits, and this code is run:
with open('highScoreFile', 'w') as file:
    print("Saving highscore to file:", highScore)
    file.write(str(highScore))
