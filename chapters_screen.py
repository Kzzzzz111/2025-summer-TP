from cmu_graphics import *

##############################
# chapters screen
##############################

def chapters_onScreenActivate(app):
    # Every time we switch to the chapters screen, reset the chapter selection
    app.selectedChapter = None

def chapters_redrawAll(app):
    drawLabel('Choose a level with your keyboard', app.width/2, 80, size=30, fill='white', bold=True)
    drawLabel('1. Chapter One', 100, 150, size=20, fill='white')
    drawLabel('2. Chapter Two', 100, 200, size=20, fill='white')
    drawLabel('3. Chapter Three', 100, 250, size=20, fill='white')
    drawLabel('Press ESC to return to the start screen', 20, app.height - 40, size=15, fill='white', align='bottom-left', opacity=60)

    # for debugging purposes, show the mouse coordinates
    drawLabel(f'Mouse: {app.mouseX}, {app.mouseY}', 20, app.height - 20, size=15, fill='white', align='bottom-left', opacity=60)

def chapters_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')
    if key == '1':
        setActiveScreen('game')
        app.selectedChapter = 1
    elif key == '2':
        setActiveScreen('game')
        app.selectedChapter = 2
    elif key == '3':
        setActiveScreen('game')
        app.selectedChapter = 3

def chapters_onMouseMove(app, mouseX, mouseY):
    # update the mouse coordinates in the app object
    app.mouseX = mouseX
    app.mouseY = mouseY