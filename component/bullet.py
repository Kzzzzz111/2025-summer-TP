from cmu_graphics import *

class Bullet:
    def __init__(self, app, type, cx, cy):
        self.type = type
        self.cx = cx+5 # cx is the mid width of the selected block, the cx of the shooter
        self.cy = cy-35 # cy is the mid height of the selected block, the cy of the shooter
        self.imageAddress = 'image/bullets/PeaNormal/PeaNormal_0.png'
        self.attack = 10
        self.appear = True
        self.hitZombie = False
        self.movingSpeed = 5
    
    def draw(self):
        if self.appear:
            drawImage(self.imageAddress, self.cx, self.cy, align = 'bottom')
    
    def move(self):
        self.cx += self.movingSpeed
    
    def update(self, app):
        if self.hitZombie:
            self.imageAddress = 'image/bullets/PeaNormalExplode/PeaNormalExplode_0.png'

    def disappear(self):
        self.appear = False

    def hit(self, zombieCx):
        if zombieCx-30 <= self.cx <= zombieCx - 10: # Incase the 20 ticks is not exact enough
            self.hitZombie = True
