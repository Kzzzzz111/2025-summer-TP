from cmu_graphics import *

def onAppStart(app):
    app.background = 'black'
    app.selectedChapter = None
    app.width = 1280
    app.height = 720
    app.mouseX = None
    app.mouseY = None
    app.selectorImage = 'image/SelectorScreen_withbutton.png'


##############################
# start screen
##############################
def start_redrawAll(app):
    titleX = 400
    titleY = app.height // 2 - 55

    # draw the background image and the start button
    drawImage(app.selectorImage, 1280, 720, align='bottom-right')
    # draw the title image (at the left center of the screen)
    drawImage('image/PvZ_Logo.jpg', titleX, titleY, align='center')
    # draw the subtitle and credit label
    drawLabel('2025 Term Project', titleX, titleY + 78, size=30, fill='white', align='center', opacity=70, bold=True, italic=True)
    drawLabel('by Kevin Meng', titleX, titleY + 108, align='center', size=15, fill='white', opacity=70, bold=True, italic=True)
    # for debugging purposes, show the mouse coordinates
    drawLabel(f'Mouse: {app.mouseX}, {app.mouseY}', 20, app.height - 20, size=15, fill='white', align='bottom-left', opacity=60)



def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('chapters')


def start_onMousePress(app, mouseX, mouseY):

    pass

def start_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY
    # check if the mouse is over the start button
    if start_isOnStartButton(app, mouseX, mouseY):
        # draw the highlighted start button
        app.selectorImage = 'image/SelectorScreen_withbutton_highlight.png'

def start_isOnStartButton(app, mouseX, mouseY):
    # Check if the mouse is within the bounds of the start button
    buttonLeft = 830
    buttonTop = 220
    buttonWidth = 300
    buttonHeight = 80

    return (buttonLeft <= mouseX <= buttonLeft + buttonWidth) and (buttonTop <= mouseY <= buttonTop + buttonHeight)

##############################
# chapters screen
##############################
def chapters_onScreenActivate(app):
    # Every time we switch to the chapters screen, reset the chapter selection
    app.selectedChapter = None

def chapters_redrawAll(app):
    drawLabel('Choose a chapter with your keyboard', app.width/2, 80, size=30, fill='black', bold=True)
    drawLabel('Press ESC to return to the start screen', app.width/2, 115, size=20, fill='black', opacity=70)
    drawLabel('1. Chapter One', 100, 150, size=20, fill='black')
    drawLabel('2. Chapter Two', 100, 200, size=20, fill='black')
    drawLabel('3. Chapter Three', 100, 250, size=20, fill='black')

def chapters_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

##############################
# game screen
##############################
def game_redrawAll(app):
    drawLabel(f'You are playing Chapter {app.selectedChapter}', app.width/2, app.height/2, size=30, fill='green')



def main():
    runAppWithScreens(initialScreen='start')



main()