# ACF Pygame Exercises (BHA)

This repository contains a variety of assignments and demos to be used by ACF (Applied Computing Foundation) coaches for the BHA (Branksome Hall Asia) summer camp.

## How To Use

Every folder represents a single day, with comments inside of every file
introducing the problem statement and templated code. To work with the code:

1. download/clone this repository
2. find a day's respective folder and its `main.py` file (and other files in the folder if provided)
3. ensure Python is installed on your computer and start coding!<br/>

_Alternatively, you may also copy the code of a file and paste it into an environment that can run Python like [the Replit website](https://replit.com/~)._

## Day-by-Day Exercises

##### Day 1: Drawing Shapes, Movement, and Frames

- Introduction to Pygame through looking at [its documentation](https://www.pygame.org/docs/)!
- `template.py`: A template that should be downloaded by students. Contains baseline code that creates an empty Pygame window.
- `001-draw.py`: Primer to Pygame that demonstrates how to draw shapes onto the screen.
  - Content: `pygame.draw.rect()`, `pygame.draw.circle()`
  - Exercise: Draw a rendition of a flag design!
- `002-move.py`: Introduction to saving global variables to store data and receiving keyboard input from the user.
  - Content: `pygame.key.get_pressed()`
  - Exercise: The code provided only shows how to receive keyboard input, and create player coordinates. Connect these up, and make the player move based on key presses!
- `003-ticks.py`: Looking into the concept of frames per second (FPS) to make games ALWAYS run at the same speed, no matter how fast one's computer is!
  - Content: `pygame.time.Clock()`, `pygame.time.Clock.tick()`
  - Exercise: Add local multiplayer functionality! Create another player, and allow that player to move around using different keys (e.g., one player uses WASD and the other uses arrow keys).

##### Day 2: Collisions and Classes

- `template.py`: A template that should be downloaded by students. Contains content that should be complete by the end of Day 1: a local multiplayer game.
- `001-collide.py`: Introduction to running code when two objects collide.
  - Content: `pygame.Rect()`, `pygame.Rect().colliderect()`
  - Exercise: Think about the problem, "Is there anything repetitive in our code that we could move elsewhere?"
- `002-classes.py`: Simplifying our main code by moving it outside into classes!
  - Content: `class Player`, `__init__()`, `draw()`, `update()`
  - Exercise: We won't fix the problem that occurs when we move our players into separate scripts, but think up a potential solution!

##### Day 3: Project Demos

- `template.py`: A template that should be downloaded by students. Contains baseline code that creates an empty Pygame window.
- `gravity-demo`: An example project that can be extended. Implements simple movement with downwards gravity.
- `image-demo`: An example project that can be extended. Demonstrates importing images from the working directory.
- `snake-demo`: An example project that can be extended. Implements Snake movement that quits when the player goes out-of-bounds.

##### Day 4: Project Development

- No contents for Day 4; instead, students should ask individual questions and plan out a self-designed project. This can potentially build off of a Pygame project started during Day 3.

<br>
<small><i>List compiled and projects developed by Lucas Wang.
</i></small>
