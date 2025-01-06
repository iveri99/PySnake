import pygame
import random

pygame.init() # Initialise pygame

# Constants
HEIGHT = 800
WIDTH = 800 
CELL_SIZE = 20
CELL_MOVEMENT = 1 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((HEIGHT,WIDTH)) # Set up screen/display
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()

class Snake:
    def __init__(self): # Initialise Snake object
        self.body = [[5,5], [4,5], [3,5]]
        self.direction = "RIGHT"
    def move(self):
        # Getting position of head
        head_x, head_y = self.body[0]
        
        # Update head position based on direction
        if self.direction == "RIGHT":
            new_head = (head_x + CELL_MOVEMENT, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - CELL_MOVEMENT, head_y)
        elif self.direction == "UP":
            new_head = (head_x, head_y - CELL_MOVEMENT)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + CELL_MOVEMENT)

        # Add new head and remove last part to create movement
        self.body = [new_head] + self.body[:-1]
        
    def draw(self,screen):
        for segment in self.body:
            x, y = segment 
            pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


        
    
    # def change_direction(self, new_direction):

snake = Snake() # Create snake object

running = True
while running: # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False # If user quits tab, game stops
    

    keys = pygame.key.get_pressed() # User input control
    if keys[pygame.K_UP] and snake.direction != "DOWN":
        snake.direction = "UP"
    if keys[pygame.K_DOWN] and snake.direction != "UP":
        snake.direction = "DOWN"
    if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
        snake.direction = "RIGHT"

    snake.move()

    screen.fill((255,245,200))
    snake.draw(screen)
    pygame.display.flip()

    clock.tick(60)

