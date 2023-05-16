# File created by Dominic Grizelj
# 1st file created by... 2nd library 3rd global functions
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
# Class bc capitalized
vec = pg.math.Vector2
# player class
# This defines the attributes of the player, like drawing it, its starting movement/spwn point
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((30,30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH - 100, HEIGHT - 100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
# This just moves the player left and right depending on what key they press by using the Player acceleration
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
# This defines jump and ensures that it only works when the player is in contact with the platforms
    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y = 1
        if hits:
            self.vel.y = -PLAYER_JUMP
# defines boundaries by setting the velocity to 0 once the sprite goes near off the screen
# I also changes the exact spot where the velocity goes to, in order to keep the player from getting stuck
    def inbounds(self):
        if self.rect.x > WIDTH -30:
            self.pos.x = WIDTH -31
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            self.pos.y = HEIGHT -25
            self.vel.y = 0
            
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            self.pos.y = 50
            self.vel.y = 0
            print("i am off the top of the screen...")
# This defines the update which is what the code is constantly checking for, which inlcludes the veloicty, position, acceleration, and inbounds
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        self.inbounds()
# This creates a class, which is a provides a means of bundling data and functionality together.Creates a new type of object, allowing new instances of that type to be made.
# The class includes giving Mob1 a certain range of speed, and ensuring it is properly displayed on screen and its size and color can be adjusted in main
class Mob1(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width 
        self.height = height 
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/3, HEIGHT/3)
        self.pos = vec(WIDTH/3, HEIGHT/3)
        self.vel = vec(randint(1,3),randint(1,3))
        self.acc = vec(1,1)
        self.cofric = 0.01
# This defines the inbounds of Mob1. Once the mob reaches the boundary, it's velocity is reverse and it goes in the oppisite direction
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
        if self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0:
            self.vel.y *= -1
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
# update just has the computer constantly check for changes in the Mob
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos
# This creates a class, which is a provides a means of bundling data and functionality together.Creates a new type of object, allowing new instances of that type to be made.
# The class includes giving Mob2 a certain range of speed (which is different from Mob1), and ensuring it is properly displayed on screen and its size and color can be adjusted in main
class Mob2(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width 
        self.height = height 
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/3, HEIGHT/3)
        self.pos = vec(WIDTH/3, HEIGHT/3)
        self.vel = vec(randint(4,6),randint(4,6))
        self.acc = vec(1,1)
        self.cofric = 0.01
# This defines the inbounds of Mob1. Once the mob reaches the boundary, it's velocity is reverse and it goes in the oppisite direction (same as Mob1)
# Unlike Mob1, when Mob2 reflects off the boundary, its velocity is multiplied by -1.04 instead of -1. The -1 makes the velocity flip and therefore the Mob goes in the oppisite direction at the same speed. 
# However, by multiplying it by -1.04 instead makes the mob get slightly faster everytime it reflects off the wall, making the game more difficult as it goes on 
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1.04
        if self.rect.x < 0:
            self.vel.x *= -1.04
        if self.rect.y < 0:
            self.vel.y *= -1.04
        if self.rect.y > HEIGHT:
            self.vel.y *= -1.04
# update just has the computer constantly check for changes in the Mob (same as Mob1)
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos
# This is the platform class. It is like a template for all platforms. 
# In main, one can see how you can use this tempelate to create platforms with different size, color, and variants
# variants are its abilities defined in main upon collision, like teleportation, or to make the win screen pop up
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
