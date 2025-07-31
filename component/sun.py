from cmu_graphics import *
import random

class Sun:
    def __init__(self, app):
        self.cx = random.choice(app.cxList)  # Randomly choose a column
        self.cy = -10  # Start above the screen
        self.appear = True
        # self.imageFolder = 'image/sun/Sun_' # There is only one folder for sun images
        self.imageIndex = 0
        self.fallingSpeed = 2  # Speed at which the sun falls
        self.value = 25

    def draw(self):
        drawImage(f'image/sun/Sun_{self.imageIndex}.png', self.cx, self.cy, align='bottom', opacity=80)

    def update(self, app):
        self.imageIndex = (app.timeIndex//2 + 1) % 21  # Loop through the zombie images

    def move(self):
        self.cy += self.fallingSpeed

    def collect(self, app):
        app.sunAmount += self.value
        self.appear = False  # Remove the sun from the screen after collecting
        app.suns.remove(self)  # Remove the sun from the list of suns