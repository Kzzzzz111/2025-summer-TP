from cmu_graphics import *
import random

class NormalZombie:
    def __init__(self, app, type):
        self.type = type  # Type of the zombie, e.g., 'NormalZombie', 'ConeheadZombie'
        self.cx = 1300
        self.cy = random.choice(app.cyList)
        self.appear = True
        if self.type == 'NormalZombie': # Normal Zombie
            self.imageFolder = 'image/zombies/NormalZombie/Zombie/Zombie_'
            self.hp = 150
        elif self.type == 'ConeheadZombie': # Conehead Zombie
            self.imageFolder = 'image/zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_'
            self.hp = 300
        self.imageIndex = 0
        self.movingSpeed = 1
        self.stop = False
        self.success = False  # Whether the zombie has reached the end of the lane
        self.dead = False
        self.attacknum = 20

    def draw(self):
        drawImage(f'{self.imageFolder}{self.imageIndex}.png', self.cx, self.cy, align='bottom')
        drawLabel(self.hp, self.cx+17, self.cy-130, fill='red', size=20, border='black', borderWidth=1)

    def update(self, app):
        self.imageIndex = (app.timeIndex//2) % 21  # Loop through the zombie images
        # change status of the zombie based on its HP
        # if self.type == 'NormalZombie':
        #     if self.hp <= 0:
        #         self.appear = False
        if self.hp <= 0:
            self.appear = False
            self.dead = True

    def move(self):
        self.cx -= self.movingSpeed

    # we don't remove the zombie from the list when it disappears, but we set its appear to False
    # so we can control the amount of zombies' appearance in the specific chapter
    def end(self): # if reach the end
        self.appear = False
        self.success = True
            
