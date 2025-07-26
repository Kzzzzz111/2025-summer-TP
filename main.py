from cmu_graphics import *

def onAppStart(app):
    app.selectedChapter = None
    app.width = 1280
    app.height = 720

##############################
# start screen
##############################
def start_redrawAll(app):
    titleX = app.width / 2
    titleY = app.height / 2 - 50

    drawLabel('PvZ special edition', titleX, titleY, size=30, fill='black', bold=True)
    drawLabel('2025 Term Project', titleX, titleY - 30, size=20, fill='black', opacity=70, bold=True)
    drawLabel('by Kevin Meng', titleX, titleY + 30, size=10, fill='black')

def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('chapters')

##############################
# chapters screen
##############################
def chapters_onScreenActivate(app):
    # Every time we switch to the chapters screen, reset the chapter selection
    app.selectedChapter = None

def chapters_redrawAll(app):
    drawLabel('Choose a chapter with your keyboard', app.width/2, 80, size=30, fill='black')
    drawLabel('1. Chapter One', 100, 150, size=20, fill='black')
    drawLabel('2. Chapter Two', 100, 200, size=20, fill='black')
    drawLabel('3. Chapter Three', 100, 250, size=20, fill='black')

def chapters_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

        

def main():
    runAppWithScreens(initialScreen='start')



main()