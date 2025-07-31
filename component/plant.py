from cmu_graphics import *

class Sunflower:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        # self.imageFolder = 'image/plants/SunFlower/SunFlower_' # There is only one folder for sunflower images
        self.imageIndex = 0
        self.fallingSpeed = 0  # Sunflowers do not fall
        self.value = 25  # Amount of sun produced by sunflower
        self.cost = 50  # Cost to plant a sunflower

    def draw(self):
        drawImage(f'image/plants/SunFlower/SunFlower_{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        self.imageIndex = (app.timeIndex//2 + 1) % 17  # Loop through the sunflower images

    def produceSun(self, app):
        app.flowerSunAmount += self.value  # Increase the sun amount