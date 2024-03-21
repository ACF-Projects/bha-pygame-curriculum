"""
This is called a class! It's a blueprint for an object.

Here, we've created a Player class that stores information
about the player's current position, as well as a few
functions to help us do things with the player!
"""

import pygame

class Player:

    def __init__(self, starting_x, starting_y):
        self.rect = pygame.Rect(starting_x, starting_y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)

    def update(self, screen):
        pressed_keys = pygame.key.get_pressed()
        ### Moves this player when WASD are pressed. ###
        if pressed_keys[pygame.K_w]:
            self.rect[1] -= 10
        if pressed_keys[pygame.K_a]:
            self.rect[0] -= 10
        if pressed_keys[pygame.K_s]:
            self.rect[1] += 10
        if pressed_keys[pygame.K_d]:
            self.rect[0] += 10
        ### Draw this player to the screen. ###
        self.draw(screen)