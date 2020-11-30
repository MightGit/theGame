import pygame



pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.mixer.music.load('Flowers for Bodysnatchers - Hearken Our Storm.mp3')  #https://soundcloud.com/synthwave80s/01-vice-point
pygame.mixer.music.play(-1)

from Player import PlayerClass
from Enemy import EnemyClass
from Terrain import TerrainClass
from Alger import AlgerClass
from FastEnemy import FastEnemyClass
from MenuBotton import ButtonMaker
from CharacterSelecter import Goldfish
from CharacterSelecter import ClownFish
from CharacterSelecter import Axolotl

from random import randint as rando
clock = pygame.time.Clock()
gameWindowHeight = 800
gameWindowWidth = 1200
powerUp = 0
fastSharkCheck = 0
MenuChecker = 1
startSpawn = 0

terrain = []
enemies = []
fastEnemies = []
algae = []


highScore = 0

tideDecider = 0
tideX = 0.0
tideY = 0.0

try:
    with open('highScoreFile') as file:
        data = file.read()
        highScore = int(data.strip())
        print("Loaded high score:", highScore)
except:
    print("highScoreFile not found, resetting to 0.")

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))


def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True

playerObject = PlayerClass(screen, xpos=590, ypos=100, terrainCollection=terrain)

def spawnEnemy():
    enemies.append(EnemyClass(screen, terrainCollection=terrain, player=playerObject))


def spawnFastEnemy():
    fastEnemies.append(FastEnemyClass(screen, terrainCollection=terrain, player=playerObject))


def createTerrain():
    terrain.append(TerrainClass(screen, rando(-200, gameWindowWidth + 200), rando(-200, gameWindowHeight + 200), rando(10, 200), rando(10, 200)))
    if collisionChecker(playerObject, terrain[-1]):
        terrain.pop()
        createTerrain()

def createAlger():
    algae.append(AlgerClass(screen, _x=rando(-100, gameWindowWidth + 100), _y=rando(-100, gameWindowHeight + 100), _width=rando(20, 75), _height=rando(20, 75)))

def restartGame():
    global MenuChecker
    MenuChecker = 1
    global startSpawn
    startSpawn = 0
    enemies.clear()
    algae.clear()
    terrain.clear()
    fastEnemies.clear()
    playerObject.height = 20
    playerObject.width = 20
    playerObject.changeSpeedToFixed(5)
    global fastSharkCheck
    fastSharkCheck = 0
    playerObject.x = 590
    playerObject.y = 100


button = ButtonMaker(screen, 500, 350, 200, 100)

Goldfish = Goldfish(screen, 50, 250, 100, 50)
ClownFish = ClownFish(screen, 50, 350, 100, 50)
Axolotl = Axolotl(screen, 50, 450, 100, 50)

done = False
while not done:
    playerObject.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        #-----------Menu------------






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
            if event.key == pygame.K_r:
                restartGame()

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
    if collisionChecker(button, playerObject):
            MenuChecker = 0
    if MenuChecker == 1 and collisionChecker(playerObject, Goldfish):
        playerObject.color = 225, 250, 25
    if MenuChecker == 1 and collisionChecker(playerObject, ClownFish) and highScore > 919:
        playerObject.color = 200, 50, 250
    if MenuChecker == 1 and collisionChecker(playerObject, Axolotl) and highScore > 39:
        playerObject.color = 250, 20, 50


    #---------Out of Menu-----------
    if MenuChecker == 0 and startSpawn == 0:
        for i in range(6):
            createAlger()

        for i in range(15):
            createTerrain()
        for i in range(5):
            spawnEnemy()
        startSpawn = 1
        tideDecider = 0


    for enemy in fastEnemies:
        enemyIsDead = False  # boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()
        enemy.enemyDeadTimer()
        if enemy.enemyTime > 120000:
            enemyIsDead = True
        if enemy.x > gameWindowWidth or enemy.y > gameWindowHeight or enemy.x < 0 or enemy.y < 0:
            enemies.remove(enemy)
        if collisionChecker(enemy, playerObject):
            playerObject.DeathSFX.play()
            print("OUCH!")
            restartGame()

        if enemyIsDead:
            enemies.remove(enemy)

    for enemy in enemies:
        enemyIsDead = False  #boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()
        enemy.enemyDeadTimer()
        if enemy.enemyTime > 1200:
            enemyIsDead = True


        if enemy.x > gameWindowWidth or enemy.y > gameWindowHeight or enemy.x < 0 or enemy.y < 0:
            enemies.remove(enemy)
        if collisionChecker(enemy, playerObject):
            playerObject.DeathSFX.play()
            print("OUCH!")
            restartGame()

        if enemyIsDead:
            enemies.remove(enemy)

    for alger in algae:
        if collisionChecker(alger, playerObject):
            algae.remove(alger)
            playerObject.collisionSFX.play()
            playerObject.points += 1
            createAlger()
            spawnEnemy()
            powerUp = rando(0, 15)
            if powerUp == 11 and playerObject.height < 20:
                playerObject.changeSpeedTo(-1)
                # print('Points:',playerObject.points)
                playerObject.height += 5
                playerObject.width += 5
            if powerUp == 10 and playerObject.height > 9:
                playerObject.height -= 5
                playerObject.width -= 5
                playerObject.changeSpeedTo(1)

    if MenuChecker == 0:
        if tideDecider % 400 == 0:
                tideX = rando(-2, 2)
                tideY = rando(-2, 2)
        if tideDecider % 400 == 0:
            spawnEnemy()

        if tideDecider % 3 == 0:
            for alger in algae:
                alger.x = alger.x - tideX
                alger.y = alger.y - tideY
            for tile in terrain:
                tile.x = tile.x - tideX
                tile.y = tile.y - tideY
        if tideDecider % 200 == 0:
            createAlger()

        if tideDecider % 100 == 0:
            createTerrain()

        if tideDecider > 1200 and fastSharkCheck == 0:
            for i in range(2):
                spawnFastEnemy()
                fastSharkCheck = 1

        #DRAW GAME OBJECTS:
    screen.fill((0, 0, 20))  #blank screen. (or maybe draw a background)

    #Score:                                                 antialias?, color
    for alger in algae:
        alger.draw()
    for enemy in fastEnemies:
        enemy.draw()

    for enemy in enemies:
        enemy.draw()

    for tile in terrain:
        tile.draw()

    playerObject.draw()
    if MenuChecker == 1:
        button.draw()

    if MenuChecker == 1 and highScore > 19:
        Goldfish.draw()
        ClownFish.draw()
        if MenuChecker == 1 and highScore > 39:
            Axolotl.draw()

    text = font.render('SCORE: ' + str(playerObject.points), True, (0, 255, 0))
    screen.blit(text, (0, 0))

    text = font.render('HIGH SCORE: ' + str(highScore), True, (255, 0, 0))
    screen.blit(text, (300, 0))

    pygame.display.flip()
    clock.tick(60)
    tideDecider = tideDecider + 1
    if playerObject.points > highScore:
        highScore = playerObject.points

#When done is false the while loop above exits, and this code is run:
with open('highScoreFile', 'w') as file:
    print("Saving high score to file:", highScore)
    file.write(str(highScore))
