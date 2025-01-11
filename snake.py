import pygame
import random

pygame.init() # Initialise pygame

# Constants
HEIGHT = 600
WIDTH = 600 
CELL_SIZE = 30
CELL_MOVEMENT = 0.5 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Define game variables
food = [0,0]
new_food = True

screen = pygame.display.set_mode((HEIGHT,WIDTH)) # Set up screen/display
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()

game_over = None # Variable created for when the game is over


class Snake:
    def __init__(self): # Initialise Snake class
        self.body = [[5,5], [4,5], [3,5], [2,5]]
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

    def get_head_position(self):
        return self.body[0] # Method for returning position of snake's head
    
    def check_wall_collision(self):
        head_x, head_y = self.get_head_position()

        head_x_pixel = head_x * CELL_SIZE # Creates a larger surface area for collision to be detected (x)
        head_y_pixel = head_y * CELL_SIZE # Creates a larger surface area for collision to be detected (y)

        if (head_x_pixel < 0 or
        head_x_pixel + CELL_SIZE > WIDTH or  # Adjust for the right edge
        head_y_pixel < 0 or
        head_y_pixel + CELL_SIZE > HEIGHT):  # Adjust for the bottom edge
            return True  # Collision detected
        return False
    
    def get_body_position(self): # Returns position the whole snake object
        return self.body
    
class Food:
    def __init__(self): # Initialise Food class 
        self.position = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)] # Positions the food at random coords (x,y)
    
    def draw(self, screen): # Method for drawing food object
        x, y = self.position
        pygame.draw.rect(
            screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
        
    def get_food_position(self): # Returns position of food object
        return self.position
        
    def check_snake_collision(self, Snake): # Checks whether snake & food are on the same coordinates
        food_x, food_y = self.position
        head_x, head_y = snake.get_head_position()

        if [food_x, food_y] == [head_x, head_y]:
            return True
        return False

    def respawn(self): # Respawns food object, and makes sure that food object isn't in the same position as the snake object
        while True:
            new_position = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
            if new_position not in snake.get_body_position:
                self.position = new_position
                break 
        
    # def respawn(self):
    # if snake When snake touches food object
        # Make food object disappear
        # Then immediately redraw food object at another random position on the grid
        
        
snake = Snake() # Create snake object
food = Food() # Create food object

FPS = 60
MOVE_SPEED = 4
frame_count = 0

running = True
while running: # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False # If user quits tab, game stops
    
    if snake.check_wall_collision(): # Conditional using snake object & method
        print("The snake hit the wall!") # Print statement
        pygame.quit() # Quits the game


    keys = pygame.key.get_pressed() # User input control
    if keys[pygame.K_UP] and snake.direction != "DOWN":
        snake.direction = "UP"
    if keys[pygame.K_DOWN] and snake.direction != "UP":
        snake.direction = "DOWN"
    if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
        snake.direction = "RIGHT"

    frame_count +=1 # Increments frame counter

    if frame_count % MOVE_SPEED == 0: # Moves the snake at desired spped
        snake.move()

    screen.fill((255,245,200)) # A slightly darker beige colour
    snake.draw(screen) # Draws the snake onto the screen
    food.draw(screen) # Draws the food object onto screen
    pygame.display.flip() # Refreshes screen

    clock.tick(FPS) # Controls how many frames per second the game runs at

