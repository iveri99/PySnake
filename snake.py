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

snake = Snake()
print(snake.body)
print(snake.direction)