# File created by Dominic Grizelj
WIDTH = 1440
HEIGHT = 900
PLAYER_ACC = 0.33
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 12
PLAYER_GRAV = 0.5
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False
FONT = "COMICS"




PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                #  (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (0,200,0), "bouncey"),
                #  (600, HEIGHT - 150, 50, 10, (200,200,200), "disappearing "),
                 (100, 750, 150, 10, (200,200,200), "normal"),
                 (300, 640, 300, 10, (200,200,200), "normal"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 13 / 20, 100, 20, (0,200,0), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 10 / 20, 100, 20, (0,200,0), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 7 / 20, 100, 20, (0,200,0), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 4 / 20, 100, 20, (0,200,0), "bouncey"),
                 (700, 440, 200, 10, (200,200,200), "normal"),
                #  (1200, 100, 2, 700, (200,200,200), "teleport"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 2 / 20, 100, 10, (100,0,0), "teleport")]

                #  (175, 100, 50, 10, (200,200,200), "normal")]
# (x position, y position, x size, y size)


# 30