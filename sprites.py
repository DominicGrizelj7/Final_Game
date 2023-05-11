# File created by Dominic Grizelj
# 1st file created by... 2nd library 3rd global functions
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
# Class bc capitalized
vec = pg.math.Vector2
# player class

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
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y = 1
        if hits:
            self.vel.y = -PLAYER_JUMP

# defines boundaries by setting the velocity to 0 once the sprite goes near off the screen
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

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        self.inbounds()


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
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
        if self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0:
            self.vel.y *= -1
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos

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
        self.vel = vec(randint(5,7),randint(5,7))
        self.acc = vec(1,1)
        self.cofric = 0.01

    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos


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



    # 49,