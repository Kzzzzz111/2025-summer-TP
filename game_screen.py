from cmu_graphics import *
from component import *
from component.zombie import *
import random

##############################
# game screen
##############################

def game_onScreenActivate(app):
    app.timeIndex = 0
    app.zombieTypes = ['NormalZombie', 'ConeheadZombie']
    app.zombies = []
    zombie1 = NormalZombie(app, random.choice(app.zombieTypes))
    app.zombies.append(zombie1)
    app.sunAmount = 100  # Initial amount of sun
    app.holdingPlant = None  # No plant is being held initially
    app.plantTypes = ['Sunflower', 'Peashooter', 'Wallnut', 'SnowPea', 'CherryBomb']

    # app.stepsPerSecond = 10 # this controls the speed of the game, 10 ticks per second
    app.stepsPerSecond = 200 # for debugging purposes, set to 50 ticks per second
    app.playerLose = False

def game_redrawAll(app):
    ###############################

    # draw the game board
    drawImage('image/background/Background_noRoad.jpg', 0, 0, align='top-left')
    
    # top-left message
    if app.selectedChapter == 1:
        drawRect(10, 10, 282, 72, fill='black', opacity=60)
        drawLabel(f'Chapter {app.selectedChapter}', 20, 20, align='top-left', size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel(f'Remaining zombies: {20 - len(app.zombies)}', 20, 52, align='top-left', size=24, fill='white', bold=True, border='black', borderWidth=1)
    else:
        drawLabel('Oops! You chose an unavailable chapter!', app.width/2, app.height/2-15, size=30, fill='white', bold=True, border='black', borderWidth=1)
        drawLabel('Please wait for the coming new version!', app.width/2, app.height/2+15, size=30, fill='white', bold=True, border='black', borderWidth=1)
    
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

    ##############################
    # game logic
    ##############################

    # draw the zombies
    # drawImage(f'image/zombies/NormalZombie/Zombie/Zombie_{app.zombieIndex}.png', 200, 200, align='center')
    for zombie in app.zombies:
        if zombie.appear and not zombie.success:
            zombie.draw()
            zombie.disappear()
        if zombie.success:
            drawLabel('The zombies have eaten your brain!', app.width/2, app.height/2, size=50, fill='red', bold=True, border='black', borderWidth=1)
            drawLabel('Press ESC to return to the chapters screen', app.width/2, app.height/2 + 60, size=20, fill='white', bold=True)

def game_onStep(app):
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

def game_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY

def game_over(app):
    app.playerLose = True
    # print("The zombies have eathen your brain!")
