from cmu_graphics import *
from component.sun import *
from component.zombie import *
from component.plant import *
from component.bullet import *
import random

##############################
# game screen
##############################

def game_onScreenActivate(app):
    app.stepsPerSecond = 20 # this controls the speed of the game, 20 ticks per second
    # app.stepsPerSecond = 1000 # for debugging purposes, set to 50 ticks per second

    app.playerLose = False  # Whether the player has lost the game
    app.sunAmount = 100  # Initial amount of sun
    app.sunAmount = 1000 # for debugging purposes, set to 1000 initial sun
    app.flowerSunAmount = 0  # Amount of sun from sunflowers
    app.timeIndex = 0

    # Initialize zombies
    app.zombieTypes = ['NormalZombie', 'ConeheadZombie']
    app.zombies = [] # List to hold zombies
    zombie1 = NormalZombie(app, random.choice(app.zombieTypes))
    app.zombies.append(zombie1)

    # Initialize suns
    app.suns = []  # List to hold suns
    sun1 = Sun(app)
    app.suns.append(sun1)

    # Initialize plants
    app.holdingPlant = None  # No plant is being held initially
    app.plantTypes = ['Sunflower', 'PeaShooter', 'WallNut', 'SnowPea', 'CherryBomb']
    app.plantCosts = {'Sunflower':50, 'PeaShooter':100, 'WallNut':50, 'SnowPea':175, 'CherryBomb':150} # dictionary to hold the costs of each plant
    app.plants = []  # List to hold planted plants

    # Initialize bullets
    app.bulletTypes = ['Normal', 'Snow']
    app.bullets = []

def game_redrawAll(app):
    # if chose 1
    if app.selectedChapter == 1:
        # draw the game board
        drawImage('image/background/Background_noRoad.jpg', 0, 0, align='top-left')
        
        # top-left message
        drawRect(10, 10, 282, 70, fill='black', opacity=60)
        drawLabel(f'Chapter {app.selectedChapter}', 20, 20, align='top-left', size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel(f'Remaining zombies: {20 - len(app.zombies)}', 20, 52, align='top-left', size=24, fill='white', bold=True, border='black', borderWidth=1)
        
        # bottom-left message
        drawRect(10, app.height - 10, 165, 50, align='bottom-left', fill='black', opacity=60)
        drawLabel('Press ESC to go back', 20, app.height - 40, size=15, fill='white', align='bottom-left', opacity=80)
        
        # for debugging purposes, show the mouse coordinates
        drawLabel(f'Mouse: {app.mouseX}, {app.mouseY}', 20, app.height - 20, size=15, fill='white', align='bottom-left', opacity=80)

        # draw the seed bank
        drawImage('image/SeedBank1.png', 300, 10, height=80, align='top-left')
        # amount of sun
        drawLabel(f'{app.sunAmount}', 338, 76, size=15, bold=True)

        # dropping plants button
        drawRect(690, 50, 60, 40, align='center', fill='red', opacity=40)
        drawRect(690, 50, 60, 40, align='center', fill=None, border='black', borderWidth=3, opacity=70)
        drawLabel('DROP', 690, 50, size=15, fill='white', bold=True)

        # print the holding plant
        drawRect(10, 120, 282, 40, align='left', fill='black', opacity=60)
        if app.holdingPlant:
            drawLabel(f'HOLDING: {app.holdingPlant}', 20, 120, align='left',fill='white', size=20, bold=True, border='black', borderWidth=1)
            drawCircle(app.mouseX, app.mouseY, 15, fill='white', opacity=70)
        else:
            drawLabel('HOLDING: None', 20, 120, align='left', fill='white', size=20, bold=True, border='black', borderWidth=1)

        # print sun from sunflowers
        drawRect(10, 165, 282, 40, align='left', fill='black', opacity=60)
        drawLabel(f'Sun from plants: {app.flowerSunAmount}', 20, 165, align='left', fill='white', size=18, bold=True, border='black', borderWidth=1)
        # draw the collect button
        drawRect(285, 165, 81, 25, align='right', fill='red', opacity=60, border='white', borderWidth=1)
        drawLabel('COLLECT', 280, 165, align='right', size=15, fill='white', bold=True)


        ##############################
        # game logic
        ##############################
        if not app.playerLose:
            # draw the suns
            for sun in app.suns:
                sun.draw()
            # draw the zombies
            for zombie in app.zombies:
                zombie.draw()
            # draw the plants
            for plant in app.plants:
                plant.draw()
        else:
            drawRect(0, app.height//2-42, app.width, 120, fill='black', opacity=20)
            drawLabel('The zombies have eaten your brain!', app.width//2, app.height//2-10, size=50, fill='red', bold=True, border='black', borderWidth=1)
            drawLabel('Press ESC to return to the chapters screen', app.width//2, app.height//2 + 50, size=20, fill='white', bold=True)
        


    else:
        drawLabel('Oops! You chose an unavailable chapter!', app.width//2, app.height//2-15, size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel('Please wait for the coming new version!', app.width//2, app.height//2+15, size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel('Press ESC to go back', app.width//2, app.height//2+45, size=30, fill='white', bold=True, border='black', borderWidth=1)

def game_onStep(app): # instructions in each tick
    # check if the player has lost
    for zombie in app.zombies:
        if zombie.success:
            app.playerLose = True
            break
    
    if not app.playerLose:
        app.timeIndex += 1

        # update the zombies
        for zombie in app.zombies:
            if not zombie.success:
                zombie.update(app)
                zombie.move()
                zombie.disappear()
        # generate new zombies but limit to the number of the chapter limit (20 for chapter 1)
        if len(app.zombies) < 20:
            if app.timeIndex % 200 == 0:  # Every 200 steps， 10 seconds
                zombie = NormalZombie(app, random.choice(app.zombieTypes))
                app.zombies.append(zombie)
        
        # update the suns
        for sun in app.suns:
            if sun.appear and sun.cy < app.height: # still falling
                sun.update(app)
                sun.move()
            else:
                sun.update(app)
        # generate new suns every 300 steps
        if app.timeIndex % 300 == 0:  # Every 300 steps, 15 seconds
            sun = Sun(app)
            app.suns.append(sun)

        # update the plants
        for plant in app.plants:
            plant.update(app)
            if isinstance(plant, Sunflower):
                # Sunflowers produce sun every 250 steps, 12.5 seconds
                if app.timeIndex % 250 == 0: 
                    plant.produceSun(app)

def game_onKeyPress(app, key):
    if key == 'escape':
        # quit()
        setActiveScreen('chapters')

def game_onMousePress(app, mouseX, mouseY):

    if app.holdingPlant is None:  # we are not holding a plant
        # check if the mouse is on the seed bank
        if 20 <= mouseY <= 85: # Seed bank area
            if 380 <= mouseX <= 430: # Sunflower
                app.holdingPlant = 'Sunflower'
            elif 432 <= mouseX <= 482: # PeaShooter
                app.holdingPlant = 'PeaShooter'
            elif 487 <= mouseX <= 535: # WallNut
                app.holdingPlant = 'WallNut'
            elif 539 <= mouseX <= 589: # Snow Pea
                app.holdingPlant = 'SnowPea'
            elif 592 <= mouseX <= 641: # CherryBomb
                app.holdingPlant = 'CherryBomb'

    else: # we are holding a plant
        # check if the mouse has pressed the drop button
        if 690 - 30 <= mouseX <= 690 + 30 and 50 - 20 <= mouseY <= 50 + 20:
            app.holdingPlant = None  # Drop the plant in hand
        # check if the mouse has pressed a plant on the lawn
        blockRow, blockCol = game_checkBlock(app, mouseX, mouseY)
        if (blockRow is not None) and (blockCol is not None): # we are pointing at a block
            # Check if the player has enough sun to plant
            if app.plantCosts[app.holdingPlant] <= app.sunAmount:
                # Create a new plant based on the holding plant type
                if app.holdingPlant == 'Sunflower':
                    newPlant = Sunflower(app, blockRow, blockCol)
                elif app.holdingPlant == 'PeaShooter':
                    newPlant = PeaShooter(app, blockRow, blockCol)
                elif app.holdingPlant == 'WallNut':
                    newPlant = WallNut(app, blockRow, blockCol)
                elif app.holdingPlant == 'SnowPea':
                    newPlant = SnowPea(app, blockRow, blockCol)
                elif app.holdingPlant == 'CherryBomb':
                    newPlant = CherryBomb(app, blockRow, blockCol)

                # deduct the sun cost of the plant
                app.sunAmount -= app.plantCosts[app.holdingPlant]
                # drop the holding plant
                app.holdingPlant = None  # Reset the holding plant
                # Add the new plant to the plants list
                app.plants.append(newPlant)

    # collect a sun
    for sun in app.suns:
        if sun.appear and sun.cx - 50 <= mouseX <= sun.cx + 50 and sun.cy - 50 <= mouseY <= sun.cy + 50:
            sun.collect(app)
            break
    
    # collet sun from sunflower
    if (204 <= mouseX <= 285) and (145 <= mouseY <= 185): # we are clicking the collect button
        game_collectFlowerSun(app)

def game_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY

def game_checkBlock(app, mouseX, mouseY):
    # Check if the mouse is on a block
    for i in range(len(app.board)):
        for j in range(len(app.board[i])):
            midX, midY = app.board[i][j]
            if midX - 50 <= mouseX <= midX + 50 and midY - 50 <= mouseY <= midY + 50:
                return i, j
    return None, None

def game_collectFlowerSun(app):
    # Collect the sun from the sunflower
    if app.flowerSunAmount > 0:
        app.sunAmount += app.flowerSunAmount
        app.flowerSunAmount = 0  # Reset the flower sun amount after collecting
