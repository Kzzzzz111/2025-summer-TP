from cmu_graphics import *

class Sunflower:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        # self.imageFolder = 'image/plants/SunFlower/SunFlower_' # There is only one folder for sunflower images
        self.imageIndex = 0
        self.value = 25  # Amount of sun produced by sunflower
        self.cost = 50  # Cost to plant a sunflower
        self.hp = 100

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

    def draw(self):
        drawImage(f'image/plants/SunFlower/SunFlower_{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        # death check
        if self.hp <= 0:
            self.appear = False
            return

        self.imageIndex = (app.timeIndex//2) % 17  # Loop through the sunflower images

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

    def produceSun(self, app):
        app.flowerSunAmount += self.value  # Increase the sun amount

class PeaShooter:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        # self.imageFolder = 'image/plants/PeaShooter/Peashooter_' # There is only one folder for peashooter images
        self.imageIndex = 0
        self.cost = 100  # Cost to plant a peashooter
        self.shootspeed = 2 # two shots in a second
        self.hp = 100

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy
    
    def draw(self):
        drawImage(f'image/plants/PeaShooter/Peashooter_{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        self.imageIndex = (app.timeIndex//2) % 12

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

class WallNut:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        self.imageFolder = 'image/plants/WallNut/WallNut/WallNut_'
        self.imageIndex = 0
        self.cost = 50  # Cost to plant
        self.shootspeed = 2 # two shots in a second
        self.hp = 900
        # self.hp = 500
        # self.hp = 200

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy
    
    def draw(self):
        drawImage(f'{self.imageFolder}{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        # death check
        if self.hp <= 0:
            self.appear = False
            return

        if self.hp >= 600:
            self.imageIndex = (app.timeIndex//2) % 15
        elif 300 <= self.hp < 600:
            self.imageFolder = 'image/plants/WallNut/WallNut_cracked1/WallNut_cracked1_'
            self.imageIndex = (app.timeIndex//2) % 10
        elif self.hp < 300:
            self.imageFolder = 'image/plants/WallNut/WallNut_cracked2/WallNut_cracked2_'
            self.imageIndex = (app.timeIndex//2) % 14
        
        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

class SnowPea:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        # self.imageFolder = 'image/plants/SnowPea/SnowPea_' # There is only one folder for snowpeashooter images
        self.imageIndex = 0
        self.cost = 175  # Cost to plant
        self.shootspeed = 2 # two shots in a second
        self.hp = 100

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy
    
    def draw(self):
        drawImage(f'image/plants/SnowPea/SnowPea_{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        # death check
        if self.hp <= 0:
            self.appear = False
            return

        self.imageIndex = (app.timeIndex//2) % 14

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

class CherryBomb:
    def __init__(self, app, blockRow, blockCol):
        self.cx, self.cy = app.board[blockRow][blockCol]  # Set the x and y coordinate based on the board layout
        self.appear = True
        # self.imageFolder = 'image/plants/CherryBomb/CherryBomb_' # There is only one folder for snowpeashooter images
        self.imageIndex = 0
        self.cost = 175  # Cost to plant
        self.shootspeed = 2 # two shots in a second
        self.hp = 100
        self.exploded = False

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy
    
    def draw(self):
        if self.imageIndex <= 6:
            drawImage(f'image/plants/CherryBomb/CherryBomb_{self.imageIndex}.png', self.cx, self.cy, align='bottom')

    def update(self, app):
        # death check
        if self.hp <= 0:
            self.appear = False
            return

        # It will not work properly if we try to stop the image here
        # Because draw runs a bunch of illegal moves before the update function stop the image
        self.imageIndex = (app.timeIndex//10)

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy


