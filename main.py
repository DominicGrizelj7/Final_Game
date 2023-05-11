# File created by Dominic Grizelj



# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: Daniel Azevedo
# Sources: Chris Cozert
# Sources: https://www.w3schools.com/python/python_variables.asp


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
        for i in range(1,8):
            m = Mob1(25,25,(250,0,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        for i in range(0,4):
            mm = Mob2(17,17,(150,0,150))
            self.all_sprites.add(mm)
            self.enemies.add(mm)
        self.cd = Cooldown()
        self.cd.timer()
        self.run()
        
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.cd.ticking()
        # print(pg.time.get_ticks())
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
                    # self.player.pos.x = hits[0].rect.right
                    # self.player.pos.x = hits[0].rect.left
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

        end_screen = False
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

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('aleo')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)

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
