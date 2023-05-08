# File created by Dominic Grizelj
# Settings of things that dont change, like screen size, colors, jump height, acceleration, gravity, friction, FPS, and font
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
GREEN = (0, 255, 0)
# blue is grey by the way
BLUE = (128,128,128)
RED = (255,50,50)
WIN = (66, 33, 22)
FPS = 60
RUNNING = True
PAUSED = False
FONT = "COMICS"



# This creates the platforms, which have a order of (x position, y position, x size, y size, (RGB color), platform type)
#Plateform type defined in main
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (100, 750, 150, 10, (200,200,200), "normal"),
                 (300, 640, 300, 10, (200,200,200), "normal"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 13 / 20, 100, 20, (0,177,77), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 10 / 20, 100, 20, (0,177,77), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 7 / 20, 100, 20, (0,177,77), "bouncey"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 4 / 20, 100, 20, (0,177,77), "bouncey"),
                 (1055, 0, 5, 475, (0,0,0), "wall"),
                 (50, 450, 100, 10, (200,200,200), "normal"),
                 (200, 400, 100, 5, (50,255,50), "very_bouncey"),
                 (200, 20, 100, 10, (255,255,0), "1_teleport"),
                 (400, 200, 100, 10, (255,255,0), "2_teleport"),
                 (600, 50, 100, 10, (255,255,0), "3_teleport"),
                 (800, 200, 100, 10, (255,255,0), "4_teleport"),
                 (950, 300, 100, 10, (200,200,200), "normal"),
                 (600, 200, 100, 10, (200,200,200), "normal"),
                 (400, 50, 100, 10, (200,200,200), "normal"),
                 (360, 200, 30, 10, (200,200,200), "normal"),
                 (50, 75, 40, 80, (WIN), "winner"),
                 (75, 115, 7, 7, (255,255,0), "normal"),
                 (WIDTH * 5 / 4 - 550, HEIGHT * 2 / 20, 100, 10, (255,51,255), "teleport"),]


