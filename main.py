# File created by Dominic Grizelj
import pygame as pg
import os
import math
# import settings 
from settings import *
from sprites import *
from math import floor
from time import sleep


# yo
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

screen = pg.display.set_mode((WIDTH, HEIGHT))
you_lose = pg.image.load(os.path.join(game_folder, 'you_lose.jpg')).convert()
lose_rect = you_lose.get_rect()


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
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,7):
            m = Mob(20,20,(250,0,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
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

    win_screen = False

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
                        self.screen.fill(BLUE)
                        if 3>2:
                            self.draw_text("YOU WIN!!!", 100, GREEN, WIDTH/2, HEIGHT/2)
                            self.draw_text("PRESS SPACE ONCE TO PLAY AGAIN", 50, RED, WIDTH/2, HEIGHT/4)
                            pg.display.flip()
                            sleep(5)
                            for event in pg.event.get():
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                        self.draw_text("5", 50, RED, WIDTH/2.2, HEIGHT/3)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("4", 50, RED, WIDTH/2.1, HEIGHT/3)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("3", 50, RED, WIDTH/2, HEIGHT/3)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("2", 50, RED, WIDTH/1.9, HEIGHT/3)
                                        pg.display.flip()
                                        sleep(1)
                                        self.draw_text("1...", 50, RED, WIDTH/1.8, HEIGHT/3)
                                        pg.display.flip()
                                        sleep(1)
                                        self.player.pos.x = 1450
                                        self.player.pos.y = 900
                                        # self.draw_text("LOADING...", 50, RED, WIDTH/2, HEIGHT/3)
                                        # pg.display.flip()





                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

# if the sprite collides with mob sprite than the program quits
        end_screen = False
        if RUNNING == True:
            hit = pg.sprite.spritecollide(self.player, self.enemies, False)
            if hit:
                print("you hit enemy")
                end_screen = True
        if end_screen == True:
            self.screen.fill(BLUE)
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
