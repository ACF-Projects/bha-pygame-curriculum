"""
Let's use classes to simplify our code! Putting
everything inside of one big while loop tends to
get really messy...

Exercise: There's a problem with the code that
          we end up with... both players move at
          the same time by the same controls!!!
          We won't be fixing this, but can you
          think of ways to solve this problem?
"""

import pygame
import player

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True

player_1 = player.Player(300, 300)
player_2 = player.Player(500, 300)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    ### Call the update function on both players! ###
    player_1.update(screen)
    player_2.update(screen)

    ### If the two players are colliding, quit the game. ###
    if player_1.rect.colliderect(player_2.rect):
        running = False
            
    pygame.display.update()  # Update the display