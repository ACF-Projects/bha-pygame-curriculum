"""
Welcome back! This program has some logic for a 
two-player local multiplayer game. One player moves
with WASD, and the other moves with the arrow keys.
Try it out!

Author: <YOUR NAME HERE>
Grade Level: <YOUR GRADE LEVEL HERE>
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True

player_1_pos = [300, 300]
player_2_pos = [500, 300]

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.rect(screen, "blue", (player_1_pos[0], player_1_pos[1], 50, 50))
    pygame.draw.rect(screen, "red", (player_2_pos[0], player_2_pos[1], 50, 50))

    ### Returns a dictionary of keys pressed IN THIS FRAME! ###
    pressed_keys = pygame.key.get_pressed()
    ### Moves player one when WASD are pressed. ###
    if pressed_keys[pygame.K_w]:
        player_1_pos[1] -= 10
    if pressed_keys[pygame.K_a]:
        player_1_pos[0] -= 10
    if pressed_keys[pygame.K_s]:
        player_1_pos[1] += 10
    if pressed_keys[pygame.K_d]:
        player_1_pos[0] += 10
    ### Moves player two when arrow keys are pressed. ###
    if pressed_keys[pygame.K_UP]:
        player_2_pos[1] -= 10
    if pressed_keys[pygame.K_LEFT]:
        player_2_pos[0] -= 10
    if pressed_keys[pygame.K_DOWN]:
        player_2_pos[1] += 10
    if pressed_keys[pygame.K_RIGHT]:
        player_2_pos[0] += 10
            
    pygame.display.update()  # Update the display