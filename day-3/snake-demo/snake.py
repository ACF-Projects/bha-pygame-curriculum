"""
This is the Snake class!

It holds all information about the Snake, like its
body (as a list of positions). It also contains 
functions that will move it across the board and
check if the player has lost.
"""

import pygame

class Snake:

    def __init__(self, screen, grid_size, tile_size):
        self.body = [(1, 0), (0, 0)]  # head position left, tail position right
        self.direction = "right"
        self.screen = screen
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.length = len(self.body)

    def grow(self):
        """
        Makes the snake grow by one. This works because the
        `update` function ONLY removes the end of the snake 
        depending on this length value.
        """
        self.length += 1

    def draw(self):
        """
        Loops through all parts of the Snake's body, and
        draws them onto the screen as squares.
        """
        for body_part in self.body:
            body_part_rect = pygame.Rect(body_part[0] * self.tile_size, body_part[1] * self.tile_size, 
                                         self.tile_size, self.tile_size)
            pygame.draw.rect(self.screen, "blue", body_part_rect) 

    def update(self):
        """
        Move the snake and call the `draw` method.

        If one of the directional arrows are pressed, move
        the snake to face in that direction.

        If the snake is hitting itself, or the wall, then
        end the game.
        """
        ### Check for key inputs and change direction if needed
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"
        if pressed_keys[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"
        if pressed_keys[pygame.K_UP] and self.direction != "down":
            self.direction = "up"
        if pressed_keys[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"
        ### Move the snake forward in its direction
        head_position = self.body[0]
        if self.direction == "left":
            head_position = (head_position[0] - 1, head_position[1])
        if self.direction == "right":
            head_position = (head_position[0] + 1, head_position[1])
        if self.direction == "up":
            head_position = (head_position[0], head_position[1] - 1)
        if self.direction == "down":
            head_position = (head_position[0], head_position[1] + 1)
        ### Check to see if we've lost
        if head_position in self.body[1:] or head_position[0] < 0 or head_position[0] >= self.grid_size or head_position[1] < 0 or head_position[1] >= self.grid_size:
            pygame.quit()
        ### Edit the snake's body to reflect this change
        if len(self.body) >= self.length:
            self.body.pop()
        self.body.insert(0, head_position)
        self.draw()