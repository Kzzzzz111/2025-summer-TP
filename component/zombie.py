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
        self.stopped = False
        self.success = False  # Whether the zombie has reached the end of the lane
        self.dead = False

        # The 4 lines below is Deepseek generated
        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

        # attack feature
        self.attacknum = 20
        self.attackInterval = 20
        self.attackCounter = 0
        self.attackingPlant = None


    def draw(self):
        drawImage(f'{self.imageFolder}{self.imageIndex}.png', self.cx, self.cy, align='bottom')
        drawLabel(self.hp, self.cx+17, self.cy-130, fill='red', size=20, border='black', borderWidth=1)

    def update(self, app):

        if self.hp <= 0:
            self.appear = False
            self.dead = True

        self.left = self.cx - 25
        self.right = self.cx + 25
        self.top = self.cy - 80
        self.bottom = self.cy

        if not self.dead: # update if it is not dead
            if not self.stopped: # walking
                if self.type == 'NormalZombie': # Normal Zombie
                    self.imageFolder = 'image/zombies/NormalZombie/Zombie/Zombie_'
                    self.imageIndex = (app.timeIndex//2) % 21  # Loop through the normal zombie images
                elif self.type == 'ConeheadZombie': # Conehead Zombie
                    self.imageFolder = 'image/zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_'
                    self.imageIndex = (app.timeIndex//2) % 20
            else: # attacking
                if self.type == 'NormalZombie': # Normal Zombie
                    self.imageFolder = 'image/zombies/NormalZombie/ZombieAttack/ZombieAttack_'
                    self.imageIndex = (app.timeIndex//2) % 20  # Loop through the normal zombie attack images
                elif self.type == 'ConeheadZombie': # Conehead Zombie
                    self.imageFolder = 'image/zombies/ConeheadZombie/ConeheadZombieAttack/ConeheadZombieAttack_'
                    self.imageIndex = (app.timeIndex//2) % 10  # Loop through the conehead zombie attack images
                self.attackCounter += 1
                if self.attackCounter >= self.attackInterval:
                    self.attackPlant()
                    self.attackCounter = 0

    def move(self):
        self.cx -= self.movingSpeed

    # we don't remove the zombie from the list when it disappears, but we set its appear to False
    # so we can control the amount of zombies' appearance in the specific chapter
    def end(self): # if reach the end
        self.appear = False
        self.success = True
    
    def attackPlant(self):
        if self.attackingPlant:
            if not self.attackingPlant.appear or self.attackingPlant.hp <= 0:
                self.stopped = False
                self.attackingPlant = None
                return
            self.attackingPlant.hp -= self.attacknum
            # reset the zombie
            if self.attackingPlant.hp <= 0:
                self.attackingPlant.appear = False
                self.stopped = False
                self.attackingPlant = None
    
