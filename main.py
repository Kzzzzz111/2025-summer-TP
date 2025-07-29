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
    # draw the subtitle
    drawImage('image/subtitle.png', titleX, titleY + 100, width=550, height=100, align='center')
    # for debugging purposes, show the mouse coordinates
    drawLabel(f'Mouse: {app.mouseX}, {app.mouseY}', 20, app.height - 20, size=15, fill='white', align='bottom-left', opacity=60)

# alternate way to go to chapters screen
def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('chapters')

def start_onMousePress(app, mouseX, mouseY):
    # check if the mouse has pressed the start button
    if start_isOnStartButton(app, mouseX, mouseY):
        setActiveScreen('chapters')

def start_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY
    # check if the mouse is over the start button
    if start_isOnStartButton(app, mouseX, mouseY):
        # draw the highlighted start button
        app.selectorImage = 'image/SelectorScreen_withbutton_highlight.png'
    else:
        # draw the normal start button
        app.selectorImage = 'image/SelectorScreen_withbutton.png'


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


##############################
# chapters screen
##############################
def chapters_onScreenActivate(app):
    # Every time we switch to the chapters screen, reset the chapter selection
    app.selectedChapter = None

def chapters_redrawAll(app):
    drawLabel('Choose a level with your keyboard', app.width/2, 80, size=30, fill='white', bold=True)
    drawLabel('Press ESC to return to the start screen', app.width/2, 115, size=20, fill='black', opacity=70)
    drawLabel('1. Chapter One', 100, 150, size=20, fill='white')
    drawLabel('2. Chapter Two', 100, 200, size=20, fill='white')
    drawLabel('3. Chapter Three', 100, 250, size=20, fill='white')

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