from cmu_graphics import *

def onAppStart(app):
    app.selectedChapter = None
    app.Background('lightblue')
    app.setSize(400, 400)
    app.setTitle('PvZ Special Edition')

##############################
# start screen
##############################
def start_redrawAll(app):
    drawLabel('PvZ special edition', 100, 100, size=30, fill='black')

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
    drawLabel('Choose a chapter:', 100, 100, size=30, fill='black')
    drawLabel('1. Chapter One', 100, 150, size=20, fill='black')
    drawLabel('2. Chapter Two', 100, 200, size=20, fill='black')
    drawLabel('3. Chapter Three', 100, 250, size=20, fill='black')

def chapters_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

        

def main():
    runAppWithScreens(initialScreen='start')



main()