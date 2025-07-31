'''
15-112 Summer 2025 Term Project
'Plants vs Zombies'
Author: Kevin Meng
'''

from cmu_graphics import *
from chapters_screen import *
from game_screen import *

def onAppStart(app):
    app.background = 'black'
    app.selectedChapter = None
    app.width = 1280
    app.height = 720
    app.mouseX = None
    app.mouseY = None
    app.selectorImage = 'image/startPage/SelectorScreen_withbutton.png'
    app.board = [
    [(350, 160), (450, 160), (545, 160), (640, 160), (735, 160), (830, 160), (925, 160), (1020, 160), (1115, 160)],
    [(350, 280), (450, 280), (545, 280), (640, 280), (735, 280), (830, 280), (925, 280), (1020, 280), (1115, 280)],
    [(350, 403), (450, 403), (545, 403), (640, 403), (735, 403), (830, 403), (925, 403), (1020, 403), (1115, 403)],
    [(350, 515), (450, 515), (545, 515), (640, 515), (735, 515), (830, 515), (925, 515), (1020, 515), (1115, 515)],
    [(350, 650), (450, 650), (545, 650), (640, 650), (735, 650), (830, 650), (925, 650), (1020, 650), (1115, 650)]]
    app.boardPlant = [[None]*9]*5
    app.cyList = [160, 280, 403, 515, 650]
    app.cxList = [350, 450, 545, 640, 735, 830, 925, 1020, 1115]

##############################
# start screen
# the function 'isOnStartButton' does not work properly in a seperate file, it may be a bug in cmu_graphics
# so I just put the start screen functions here
##############################

def start_redrawAll(app):
    titleX = 400
    titleY = app.height // 2 - 55

    # draw the background image and the start button
    drawImage(app.selectorImage, 1280, 720, align='bottom-right')
    # draw the title image (at the left center of the screen)
    drawImage('image/startPage/PvZ_Logo.jpg', titleX, titleY, align='center')
    # draw the subtitle
    # drawImage('image/startPage/subtitle.png', titleX, titleY + 100, width=550, height=100, align='center')

    # for debugging purposes, show the mouse coordinates
    drawLabel(f'Mouse: {app.mouseX}, {app.mouseY}', 20, app.height - 20, size=15, fill='white', align='bottom-left', opacity=60)

def start_onKeyPress(app, key):
    if key == 'space':
        # alternative way to go to chapters screen
        setActiveScreen('chapters')

def start_onMousePress(app, mouseX, mouseY):
    # check if the mouse has pressed the start button
    if start_isOnStartButton(app, mouseX, mouseY):
        setActiveScreen('chapters')

def start_isOnStartButton(app, mouseX, mouseY):
    # topEdge -> y = 0.140625x+173.28125
    # bottomEdge -> y = 0.0746269x + 158.0597
    # leftEdge -> y = y=0.307229x
    # rightEdge -> y = -6x + 7235
    # top-left: (830, 220)
    # top-right: (1165, 245)
    # buttom-left: (830, 290)
    # buttom-right: (1150, 335)

    # Check if the mouse is within the bounds of the start button
    return (mouseY <= 0.140625*mouseX+173.28125) and \
            (mouseY >= 0.0746269*mouseX + 158.0597) and \
            (mouseX >= 830) and \
            (mouseX <= (mouseY - 7235)/-6)

def start_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY
    # check if the mouse is over the start button
    if start_isOnStartButton(app, mouseX, mouseY):
        # draw the highlighted start button
        app.selectorImage = 'image/startPage/SelectorScreen_withbutton_highlight.png'
    else:
        # draw the normal start button
        app.selectorImage = 'image/startPage/SelectorScreen_withbutton.png'

##############################
# main function to run the app
##############################

def main():
    runAppWithScreens(initialScreen='start')

main()