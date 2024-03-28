"""
This is the Player class!

It holds all information about the Player, like its
position and movement variables. It also contains 
functions that allow the player to move around.
"""

import pygame

class Player:

    def __init__(self, screen):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.velocity = [0, 0]
        self.gravity_scale = 0.5
        self.move_speed = 8
        self.jump_speed = 10
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, "blue", self.rect)

    def update(self, platforms):
        """
        Contains logic that moves the player.

        Also draws the player onto the screen.
        """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.velocity[0] = self.move_speed * -1
        if keys_pressed[pygame.K_RIGHT]:
            self.velocity[0] = self.move_speed
        if keys_pressed[pygame.K_UP]:
            self.velocity[1] = self.jump_speed
        ### Naturally decrease velocity. ###
        self.velocity[0] *= 0.8
        ### Move the player based on velocity values. ###
        self.rect.x += self.velocity[0]
        self.rect.y -= self.velocity[1]
        ### Check if the player is colliding with any platforms. ###
        is_colliding = None
        for platform in platforms:
            if self.rect.colliderect(platform):
                is_colliding = platform
                break
        if is_colliding is not None:
            self.velocity[1] = 0
            self.rect.bottom = platform.top
        else:
            self.velocity[1] -= self.gravity_scale
        ### Draw the player onto the screen. ###
        self.draw()