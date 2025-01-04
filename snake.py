import pygame
import random

pygame.init() # Initialise pygame

# Constants
HEIGHT = 600
WIDTH = 800 
CELL_SIZE = 20 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((HEIGHT,WIDTH)) # Set up screen/display
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()

class Snake:
    def __init__(self): # Initialise Snake object
        self.body = [[100,100], [90,100], [80,100]]
        self.direction = "RIGHT"
    def move(self):
        # Getting position of head
        head_x, head_y = self.body[0]
        
        # Update head position based on direction
        if self.direction == "RIGHT":
            new_head = (head_x + 10, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - 10, head_y)
        elif self.direction == "UP":
            new_head = (head_x, head_y + 10)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y - 10)

        # Add new head and remove last part to create movement
        self.body.insert(0, new_head)
        self.body.pop()
    
    





snake = Snake()

screen.fill((255,245,200))
pygame.display.flip()

running = True
while running: # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

