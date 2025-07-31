from cmu_graphics import *

class Bullet:
    def __init__(self, app, type, cx, cy):
        self.type = type
        self.cx = cx+5 # cx is the mid width of the selected block, the cx of the shooter
        self.cy = cy-35 # cy is the mid height of the selected block, the cy of the shooter
        if self.type == 'Normal':
            self.imageAddress = 'image/bullets/PeaNormal/PeaNormal_0.png'
        else: # SnowPea
            self.imageAddress = 'image/bullets/PeaSnow/PeaSnow_0.png'
        self.attack = 10
        self.attack = 50 # for debugging purposes
        self.appear = True
        self.hitZombie = False
        self.movingSpeed = 5
        self.explodeCounter = 0
        self.explodeDuration = 5 # explode image last for 5 ticks
    
    def draw(self):
        drawImage(self.imageAddress, self.cx, self.cy, align = 'bottom')
    
    def move(self):
        self.cx += self.movingSpeed
    
    def update(self, app):
        if self.hitZombie:
            self.imageAddress = 'image/bullets/PeaNormalExplode/PeaNormalExplode_0.png'
            self.explodeCounter += 1  # 每帧增加计数
            
            # disappear after time is up
            if self.explodeCounter >= self.explodeDuration:
                self.disappear()

    def disappear(self):
        self.appear = False

    def hit(self):
        print('hit!') # for debugging pupose
        self.hitZombie = True
