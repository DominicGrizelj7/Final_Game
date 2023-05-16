# File created by Dominic Grizelj
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: Daniel Azevedo
# Sources: Chris Cozert
# Sources: David Charles
# Sources: https://www.w3schools.com/python/python_variables.asp
# Sources: https://www.w3schools.com/python/python_operators.asp
# Sources: https://www.w3schools.com/python/python_for_loops.asp
# Sources: https://www.w3schools.com/python/python_functions.asp

# import libraries and settings
import pygame as pg
import os
import math
from settings import *
from sprites import *
from math import floor
from time import sleep
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
screen = pg.display.set_mode((WIDTH, HEIGHT))
# This defines the time within the game
class Cooldown():
        def __init__(self):
            self.current_time = 0
            self.event_time = 0
        def ticking(self):
            self.current_time = floor((pg.time.get_ticks())/1000)
            self.delta = self.current_time - self.event_time
        def timer(self):
            self.current_time = floor((pg.time.get_ticks())/1000)
# create game class in order to pass properties to the sprites file and to organize
# class has properties and set methods which allow sprites to do different things
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
        self.font_name = pg.font.match_font(FONT)
# This assigns the group to its parameters/variables
# It also adds the mobs and platforms from the sprites to the actual game 
# It uses range to give how many mobs there are and defines its color
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,8):
            m = Mob1(25,25,(250,0,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        for i in range(0,3):
            mm = Mob2(17,17,(150,0,150))
            self.all_sprites.add(mm)
            self.enemies.add(mm)
        self.cd = Cooldown()
        self.cd.timer()
        self.run()
# Updating pixels of these methods
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
# This deines the different type fof platfroms and what happens once the player collides with each
# dissaperaing "kills" the platrom once collided
# bouncey makes the player jump automaticly using the PLAYER JUMP from setting
# very_bouncey does the same thing, except it multiplies the jump velocity by 4
# wall is simply a platform that is more like a boundary. you cannot go through it and you do not get teleported to the top of it once you hit it. 
# all of the teleports simply move the player to another location once it collides 
# winner makes the win screen True (win screen commented on below)
# The else at the bottom makes sure that if the player hits a platform that is not defined, it will just sit on top of it
    def update(self):
        self.all_sprites.update()
        self.cd.ticking()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = - PLAYER_JUMP 
                elif hits[0].variant == "very_bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = - PLAYER_JUMP * 4
                elif hits[0].variant == "wall":
                    self.player.vel.x = 0
                elif hits[0].variant == "teleport":
                    self.player.pos.x = 100
                    self.player.pos.y = 250
                elif hits[0].variant == "1_teleport":
                    self.player.pos.x = 400
                    self.player.pos.y = 150
                elif hits[0].variant == "2_teleport":
                    self.player.pos.x = 600
                    self.player.pos.y = 50
                elif hits[0].variant == "3_teleport":
                    self.player.pos.x = 800
                    self.player.pos.y = 150
                elif hits[0].variant == "4_teleport":
                    self.player.pos.x = 1000
                    self.player.pos.y = 50
                elif hits[0].variant == "winner":
                    self.player.pos.x = hits[0].rect.top
                    win_screen = True
# win screen makes a new screen over the game by screen.fill(BLACK) and then draws messages letting you know that you won and if you want to quit or retry
# It sleeps, or does nothing for 5 seconds to avoid the screen from flickering
# If you hit space it will retry. Once the 5 second sleep is over it will draw a countdown from 5 with 1 second sleep in between each number to make it count down
# Once it has counted down, it will move the player back into the game at a certain spot
# If the player hits escape, the game will quit once the 5 second sleep is over
                    if win_screen == True:
                        self.screen.fill(BLACK)
                        if 3>2:
                            self.draw_text("YOU WIN!!!", 250, GREEN, WIDTH/2, HEIGHT/3)
                            self.draw_text("PRESS SPACE ONCE TO PLAY AGAIN", 25, RED, WIDTH/2, HEIGHT/2)
                            self.draw_text("PRESS ESCAPE TO QUIT", 25, RED, WIDTH/2, HEIGHT/1.9)
                            pg.display.flip()
                            sleep(5)
                            for event in pg.event.get():
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                        self.draw_text("5", 50, RED, WIDTH/2.2, HEIGHT/1.5)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("4", 50, RED, WIDTH/2.1, HEIGHT/1.5)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("3", 50, RED, WIDTH/2.0, HEIGHT/1.5)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("2", 50, RED, WIDTH/1.9, HEIGHT/1.5)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("1...", 50, RED, WIDTH/1.8, HEIGHT/1.5)
                                        pg.display.flip()
                                        sleep(1)
                                        self.player.pos.x = 1450
                                        self.player.pos.y = 900 
                                    if event.key == pg.K_ESCAPE:
                                        pg.quit()
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
# This makes the endscreen false at all times unless the player hits a "win" platform as defined above 
        end_screen = False
# This says the if the player collides with an enemy, which is the Mob1 and Mob2 class, it will fill the screen black and draw Try again for 1 second while it sleeps. 
# After the 1 second sleep is over, the player will be moved to 
        if RUNNING == True:
            hit = pg.sprite.spritecollide(self.player, self.enemies, False)
            if hit:
                print("you hit enemy")
                end_screen = True
        if end_screen == True:
            self.screen.fill(BLACK)
            if 5 > 2:
                self.player.pos.x = 1450
                self.player.pos.y = 900
                self.draw_text("TRY AGAIN", 100, RED, WIDTH/2, HEIGHT/2)
                pg.display.flip()
                sleep(1)
# This defines all the events, like jumping if you press space and what happens if you quit
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
# This defines the draw ability by giving its its font and how it will render/blit on screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('aleo')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)
# this draws the background in BLUE, which is actually grey and draws text that says "door of winners" to make the end goal of the game obvious
    def draw(self):
        self.screen.fill(BLUE)
        if 5 > 2:
            self.draw_text("DOOR OF WINNERS", 22, BLACK, WIDTH -1365, HEIGHT -860)
            self.all_sprites.draw(self.screen)
            pg.display.flip()    
# instantiate the game class...
g = Game()
# kick off the game loop
while g.running:
    g.new()
pg.quit()
