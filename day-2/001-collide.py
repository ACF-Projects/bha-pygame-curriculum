"""
Let's make our two rectangles collide! For now,
let's make it so the game quits if they ever
touch each other.

Exercise: What is one thing you notice about this
          code that seems repetitive? Anything we
          could simplify?
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True

player_1_rect = pygame.Rect(300, 300, 50, 50)
player_2_rect = pygame.Rect(500, 300, 50, 50)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.rect(screen, "blue", player_1_rect)
    pygame.draw.rect(screen, "red", player_2_rect)

    ### Returns a dictionary of keys pressed IN THIS FRAME! ###
    pressed_keys = pygame.key.get_pressed()
    ### Moves player one when WASD are pressed. ###
    if pressed_keys[pygame.K_w]:
        player_1_rect[1] -= 10
    if pressed_keys[pygame.K_a]:
        player_1_rect[0] -= 10
    if pressed_keys[pygame.K_s]:
        player_1_rect[1] += 10
    if pressed_keys[pygame.K_d]:
        player_1_rect[0] += 10
    ### Moves player two when arrow keys are pressed. ###
    if pressed_keys[pygame.K_UP]:
        player_2_rect[1] -= 10
    if pressed_keys[pygame.K_LEFT]:
        player_2_rect[0] -= 10
    if pressed_keys[pygame.K_DOWN]:
        player_2_rect[1] += 10
    if pressed_keys[pygame.K_RIGHT]:
        player_2_rect[0] += 10

    ### If the two players are colliding, quit the game. ###
    if player_1_rect.colliderect(player_2_rect):
        running = False
            
    pygame.display.update()  # Update the display