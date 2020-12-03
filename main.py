import pygame

pygame.init()  #Starting the Music in the game
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.mixer.music.load('Flowers for Bodysnatchers - Hearken Our Storm.mp3')
pygame.mixer.music.play(-1)

from Player import PlayerClass  #This is all the imports we do for the game as the other files
from Enemy import EnemyClass
from Terrain import TerrainClass
from Alger import AlgerClass
from FastEnemy import FastEnemyClass
from MenuBotton import ButtonMaker
from MenuBotton import Bagground
from MenuBotton import GameBagground
from CharacterSelecter import Goldfish
from CharacterSelecter import ClownFish
from CharacterSelecter import Axolotl
from random import randint as rando  #This is a Function to make random INT numbers


clock = pygame.time.Clock()
gameWindowHeight = 800  #Is the size of the game window
gameWindowWidth = 1200

powerUp = 0  #Here's all the Variables we use.
fastSharkCheck = 0 #Make sure Fash Sharks only spawn ones
MenuChecker = 1 #To check if players are on the Menu
startSpawn = 0 #Spawn the obj for the beginning
highScore = 0  #Highscore of the game
tideDecider = 0  #This is a TickCounter
tideX = 0.0 #The Variables we use for tides to move Obj
tideY = 0.0
 #Groups for Objects
terrain=[]
enemies=[]
fastEnemies=[]
algers=[]



#Making the highscore file
try:
    with open('highScoreFile') as file:
        data = file.read()
        highScore=int(data.strip())
        print("Loaded highscore:",highScore)
except:
    print("highScoreFile not found, resetting to 0.")

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

#This is the function to check if two game objects are touching each other
def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True
#Making of Player character
playerObject = PlayerClass(screen,xpos=590, ypos=700,terrainCollection=terrain)
#Function to spawn sharks
def spawnEnemy():
    enemies.append(EnemyClass(screen,terrainCollection=terrain,player=playerObject))

#Function to spawn Fast Sharks
def spawnFastEnemy():
    fastEnemies.append(FastEnemyClass(screen,terrainCollection=terrain,player=playerObject))

#The creation of Trash
def createTerrain():
    terrain.append(TerrainClass(screen, rando(-200,gameWindowWidth + 200),rando(-200,gameWindowHeight + 200),rando(10,200),rando(10,200)))
    if collisionChecker(playerObject, terrain[-1]):
        terrain.pop()
        createTerrain()

def createAlger():
    algers.append(AlgerClass(screen, _x= rando(-100,gameWindowWidth+100), _y=rando(-100,gameWindowHeight+100),_width=rando(20,75) ,_height=rando(20,75)))
#Function we use for sending the player back to menu
def restartGame():
    global MenuChecker
    MenuChecker = 1
    global startSpawn
    startSpawn = 0
    enemies.clear()
    algers.clear()
    terrain.clear()
    fastEnemies.clear()
    playerObject.height = 20
    playerObject.width = 20
    playerObject.changeSpeedToFixed(5)
    global fastSharkCheck
    fastSharkCheck = 0
    playerObject.x = 590
    playerObject.y = 700
    playerObject.points=0
    playerObject.goldfishSize = playerObject.goldfishIMG20
    playerObject.AxolotlSize = playerObject.AxolotlIMG20
    playerObject.clownfishSize = playerObject.clownfishIMG20


def player(x, y):
    screen.blit(playerObject.goldfishSize, (x, y))

#The buttons in Menu
botton =ButtonMaker(screen, 450,500)
Goldfish = Goldfish(screen, 50,250)
ClownFish = ClownFish(screen, 50,350)
Axolotl = Axolotl(screen, 50,450)
menuBag = Bagground(screen, 0, 0)
GameBag = GameBagground(screen, 0, 0)
#Starting Pygame loop
done = False
while not done:
    player(playerObject.x,playerObject.y)
    playerObject.update()
    #Making sure event happen in order
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
    if collisionChecker(botton, playerObject): #Checking if player touches Start button
            MenuChecker = 0
    if MenuChecker == 1 and collisionChecker(playerObject, Goldfish): #Changing player module
        playerObject.whatFish = 1
    if MenuChecker == 1 and collisionChecker(playerObject, ClownFish) and highScore > 19:
        playerObject.whatFish = 2
    if MenuChecker == 1 and collisionChecker(playerObject, Axolotl) and highScore > 39:
        playerObject.whatFish = 3


    #---------Out of Menu-----------
    if MenuChecker == 0 and startSpawn == 0: #Creating objects at start
        for i in range(6):
            createAlger()

        for i in range(20):
            createTerrain()
        for i in range(5):
            spawnEnemy()
        startSpawn = 1
        tideDecider = 0


    for enemy in fastEnemies: #Fast enemies and enemies are identical except for speed, and that fast enemies dont die
        enemyIsDead = False  # boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()
        enemy.enemyDeadTimer()
        if enemy.enemyTime > 120000:
            enemyIsDead = True
        if enemy.x > gameWindowWidth or enemy.y > gameWindowHeight or enemy.x < 0 or enemy.y < 0:
            enemies.remove(enemy)
        if collisionChecker(enemy, playerObject):
            playerObject.DeathSFX.play()
            restartGame()

        if enemyIsDead:
            enemies.remove(enemy)

    for enemy in enemies:
        enemyIsDead = False  #boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()
        enemy.enemyDeadTimer()
        if enemy.enemyTime > 1200:
            enemyIsDead = True


        if enemy.x>gameWindowWidth or enemy.y>gameWindowHeight or enemy.x<0 or enemy.y<0:
            enemies.remove(enemy)
        if collisionChecker(enemy,playerObject):
            playerObject.DeathSFX.play()
            restartGame()

        if enemyIsDead:
            enemies.remove(enemy)

    for alger in algers:
        if collisionChecker(alger,playerObject):
            algers.remove(alger)
            playerObject.collisionSFX.play()
            playerObject.points +=1
            createAlger()
            spawnEnemy()
            powerUp = rando(0, 15) #Making a random power up, but for all mldules since the size of the player is determined by Module
            if powerUp == 1 and playerObject.clownfishSize == playerObject.clownfishIMG10 and playerObject.whatFish == 2:
                playerObject.changeSpeedTo(-1)
                playerObject.clownfishSize = playerObject.clownfishIMG20
                playerObject.powerUpSFC.play()
            if powerUp == 1 and playerObject.AxolotlSize == playerObject.AxolotlIMG10 and playerObject.whatFish == 3:
                playerObject.changeSpeedTo(-1)
                playerObject.powerUpSFC.play()
                playerObject.AxolotlSize= playerObject.AxolotlIMG20
            if powerUp == 1 and playerObject.goldfishSize == playerObject.goldfishIMG10 and playerObject.whatFish == 1:
                playerObject.changeSpeedTo(-1)
                playerObject.goldfishSize = playerObject.goldfishIMG20
                playerObject.powerUpSFC.play()

            if powerUp == 2 and playerObject.clownfishSize == playerObject.clownfishIMG20 and playerObject.whatFish == 2:
                playerObject.changeSpeedTo(1)
                playerObject.clownfishSize = playerObject.clownfishIMG10
                playerObject.powerUpSFC.play()
            if powerUp == 2 and playerObject.AxolotlSize == playerObject.AxolotlIMG20 and playerObject.whatFish == 3:
                playerObject.changeSpeedTo(1)
                playerObject.AxolotlSize = playerObject.AxolotlIMG10
                playerObject.powerUpSFC.play()
            if powerUp == 2 and playerObject.goldfishSize == playerObject.goldfishIMG20 and playerObject.whatFish == 1:
                playerObject.changeSpeedTo(1)
                playerObject.goldfishSize = playerObject.goldfishIMG10
                playerObject.powerUpSFC.play()

    if MenuChecker == 0: #Loop to make sure we only spawn when MenuChecker is 0
        if tideDecider % 400 == 0: #Many spawns are tied to time Through ticks
                tideX = rando(-2,2) #The direction of the tides
                tideY = rando(-2,2)
        if tideDecider % 400 == 0:
            spawnEnemy()

        if tideDecider % 3 == 0: #Moving all Trash and Algae by the value of the random tide
            for alger in algers:
                alger.x = alger.x - tideX
                alger.y = alger.y - tideY
            for tile in terrain:
                tile.x = tile.x - tideX
                tile.y = tile.y - tideY
        if tideDecider % 200 == 0:
            createAlger()

        if tideDecider % 100 == 0:
            createTerrain()

        if playerObject.points > 19 and fastSharkCheck == 0: #Spawning sharks when player hits 20 score
            for i in range(2):
                spawnFastEnemy()
                fastSharkCheck = 1

        #DRAW GAME OBJECTS:
    screen.fill((0, 0, 20)) #Først så maler vi skærmen blank
    if MenuChecker == 1: #Her tjekker vi bare om vi er på hovedemenuen, og sørger for at tegne den rigtige baggrund
        menuBag.draw() #Baggrunden på menuen
    if MenuChecker == 0:
        GameBag.draw() #Baggrunden når spillet er i gang

   #Her tegner vi alle de objekter vi har i spillet.
    for alger in algers: #Her bruger vi For, som tager hvert obejkt i listen og tegner dem.
        alger.draw()
    for enemy in fastEnemies: #Vi har to forskellige hajer som tegnes efter hinanden
        enemy.draw()

    for enemy in enemies:
        enemy.draw()

    for tile in terrain: #Det her er alt skraldet
        tile.draw()

    playerObject.draw() #Vi tegner dem i en bestemt rækkefølge for at sørger for at hajer kan gemme sig i skrald
    if MenuChecker == 1:
        botton.draw()

    if MenuChecker ==1 and highScore > 19:
        Goldfish.draw()
        ClownFish.draw()
        if MenuChecker == 1 and highScore > 39:
            Axolotl.draw()

    text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
    screen.blit(text,(0,770))

    text = font.render('HIGHSCORE: ' + str(highScore), True, (255, 0, 0))
    screen.blit(text, (910,770))

    pygame.display.flip()
    clock.tick(60)
    tideDecider = tideDecider + 1
    if playerObject.points > highScore:
        highScore = playerObject.points

#When done is false the while loop above exits, and this code is run:
with open('highScoreFile', 'w') as file:
    print("Saving highscore to file:", highScore)
    file.write(str(highScore))
