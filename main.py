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