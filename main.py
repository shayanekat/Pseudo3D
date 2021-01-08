"""
Shayane Katchera

Pseudo 3D project
"""

# TODO (08/01/2021): 
#    - init window
#    - init maze
#    - ray casting
#    - pseudo 3D

import pygame
# =========================BACKEND=========================
# parameters
WindowSize = 500
MapSizeBlock = 20
WalkDistance = 25

# init
Walls = []
PlayerPos = []
player = ""
Exit = []

# map design
rdc = ["WWWWWWWWWWWWWWWWWWWW",
       "W   W              W",
       "W W W WWWWWWWWWWWW W",
       "W W W W            W",
       "W W   W W WWWWWWWWWW",
       "W WWWWW W W        W",
       "W W     W   WWWWWW W",
       "W W WWWWWWWWW    W W",
       "W W           WW W W",
       "W WWWWWWWWWWWWWW W W",
       "W        P   W   W W",
       "W WWWWWWWWWW W WWW W",
       "W          W W   W W",
       "W WWWWWWWW W WWWWW W",
       "W W        W W   W W",
       "W W  WWWWWWW W W W W",
       "W WW W     W W W   W",
       "W  WWW W WWW W WWWWW",
       "WW     W     W     S",
       "WWWWWWWWWWWWWWWWWWWW"]

# functions
def hauteur(distance):
    """
    Fonction qui donne la hauteur des objets en fonction de la distance
    """
    pass


# =========================FRONTEND=========================
# init display
pygame.init()
screen = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("My Game")

# main loop
running = True
while running:
    pygame.display.flip()

    # events check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for closing window
            running = False