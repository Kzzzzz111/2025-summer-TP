from cmu_graphics import *
from component import *
from component.zombie import *
import random

##############################
# game screen
##############################

def game_onScreenActivate(app):
    # app.stepsPerSecond = 10 # this controls the speed of the game, 10 ticks per second
    app.stepsPerSecond = 1000 # for debugging purposes, set to 50 ticks per second

    app.sunAmount = 100  # Initial amount of sun
    app.timeIndex = 0

    app.zombieTypes = ['NormalZombie', 'ConeheadZombie']
    app.zombies = []
    zombie1 = NormalZombie(app, random.choice(app.zombieTypes))
    app.zombies.append(zombie1)


    app.holdingPlant = None  # No plant is being held initially
    app.plantTypes = ['Sunflower', 'Peashooter', 'Wallnut', 'SnowPea', 'CherryBomb']

    app.playerLose = False

def game_redrawAll(app):
    # if chose 1
    if app.selectedChapter == 1:
        # draw the game board
        drawImage('image/background/Background_noRoad.jpg', 0, 0, align='top-left')
        
        # top-left message
        drawRect(10, 10, 282, 72, fill='black', opacity=60)
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

        # dropping plants in hand
        drawRect(690, 50, 60, 40, align='center', fill='red', opacity=40)
        drawRect(690, 50, 60, 40, align='center', fill=None, border='black', borderWidth=3, opacity=70)
        drawLabel('DROP', 690, 50, size=15, fill='white', bold=True)

        # print the holding plant
        drawRect(10, 110, 282, 40, align='left', fill='black', opacity=60)
        if app.holdingPlant:
            drawLabel(f'HOLDING: {app.holdingPlant}', 20, 110, align='left',fill='white', size=20, bold=True, border='black', borderWidth=1)
            drawCircle(app.mouseX, app.mouseY, 15, fill='white', opacity=70)
        else:
            drawLabel('HOLDING: None', 20, 110, align='left', fill='white', size=20, bold=True, border='black', borderWidth=1)

        ##############################
        # game logic
        ##############################

        # draw the zombies
        for zombie in app.zombies:
            if not app.playerLose:
                zombie.draw()
                zombie.disappear()
            else:
                drawRect(0, app.height//2-42, app.width, 120, fill='black', opacity=20)
                drawLabel('The zombies have eaten your brain!', app.width//2, app.height//2-10, size=50, fill='red', bold=True, border='black', borderWidth=1)
                drawLabel('Press ESC to return to the chapters screen', app.width//2, app.height//2 + 50, size=20, fill='white', bold=True)
        


    else:
        drawLabel('Oops! You chose an unavailable chapter!', app.width//2, app.height//2-15, size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel('Please wait for the coming new version!', app.width//2, app.height//2+15, size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel('Press ESC to go back', app.width//2, app.height//2+45, size=30, fill='white', bold=True, border='black', borderWidth=1)

def game_onStep(app):
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
        
        # generate new zombies but limit to the number of the chapter limit (20 for chapter 1)
        if len(app.zombies) < 20:
            if app.timeIndex % 200 == 0:  # Every 200 steps， 10 seconds
                zombie = NormalZombie(app, random.choice(app.zombieTypes))
                app.zombies.append(zombie)


def game_onKeyPress(app, key):
    if key == 'escape':
        # quit()
        setActiveScreen('chapters')

def game_onMousePress(app, mouseX, mouseY):
    # check if the mouse has pressed the drop button
    if 690 - 30 <= mouseX <= 690 + 30 and 50 - 20 <= mouseY <= 50 + 20:
        app.holdingPlant = None  # Drop the plant in hand

    # check if the mouse has pressed a plant in the seed bank
    if 20 <= mouseY <= 85:
        if 380 <= mouseX <= 430: # Sunflower
            app.holdingPlant = 'Sunflower'
        elif 432 <= mouseX <= 482: # Peashooter
            app.holdingPlant = 'Peashooter'
        elif 487 <= mouseX <= 535: # Wallnut
            app.holdingPlant = 'Wallnut'
        elif 539 <= mouseX <= 589: # Snow Pea
            app.holdingPlant = 'SnowPea'
        elif 592 <= mouseX <= 641: # Cherry Bomb
            app.holdingPlant = 'CherryBomb'

def game_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY
