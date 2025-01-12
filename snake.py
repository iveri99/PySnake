import pygame
import random
import sys
import pygame.freetype

# Constants
HEIGHT = 600
WIDTH = 600 
CELL_SIZE = 30
CELL_MOVEMENT = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BACKGROUND = (255,245,200)
LINES_COLOUR = (169,149,123)
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Constants for menu
OVERLAY_COLOR = (0, 0, 0, 128)  # Black with 50% transparency
BUTTON_COLOR = (200, 0, 0)  # Red button color
BUTTON_HOVER_COLOR = (255, 50, 50)  # Lighter red for hover
BUTTON_TEXT_COLOR = (255, 255, 255)  # White text
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class Snake:
    def __init__(self): # Initialise Snake class
        self.body = [[5,5], [4,5], [3,5], [2,5]]
        self.direction = "RIGHT"
        self.speed = CELL_SIZE // 5  # Pixels to move per frame (adjust for smoothness)
        self.target_position = None  # Target position for the head

    def move(self):
        # if self.target.position
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
    
    def grow(self): # Appends the snake by one cell size
        tail = self.body[-1]
        self.body.append(tail)
    
    def check_self_collision(self):
        head_x, head_y = self.get_head_position()
        
        for segment_x, segment_y in self.body[1:]:
            if (head_x == segment_x and
                head_y == segment_y):
                return True
            
        return False

    
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
        
    def check_snake_collision(self, snake): # Checks whether snake & food are on the same coordinates
        food_x, food_y = self.position
        head_x, head_y = snake.get_head_position()

        if [food_x, food_y] == [head_x, head_y]:
            return True
        return False

    def respawn(self, snake): # Respawns food object in a 'free' space on the grid
        all_positions = [
            [x, y] for x in range(COLS) for y in range(ROWS)
        ]
        snake_positions = set(tuple(pos) for pos in snake.get_body_position())
        free_positions = [pos for pos in all_positions if tuple(pos) not in snake_positions]

        if free_positions:
            self.position = random.choice(free_positions)
        else:
            raise RuntimeError("No free position available for food.")

def drawGrid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINES_COLOUR, rect, 1)

def play_again(screen):
    # Translucent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_COLOR)
    screen.blit(overlay, (0, 0))

    # Button positions
    play_again_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - 60, BUTTON_WIDTH, BUTTON_HEIGHT)
    quit_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)

    font = pygame.font.Font(None, 36)

    while True:
        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()

        # Play Again Button
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR if play_again_rect.collidepoint(mouse_pos) else BUTTON_COLOR, play_again_rect)
        play_again_text = font.render("Play Again", True, BUTTON_TEXT_COLOR)
        screen.blit(play_again_text, (play_again_rect.x + 38, play_again_rect.y + 12))

        # Quit Button
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR if quit_rect.collidepoint(mouse_pos) else BUTTON_COLOR, quit_rect)
        quit_text = font.render("Quit", True, BUTTON_TEXT_COLOR)
        screen.blit(quit_text, (quit_rect.x + 70, quit_rect.y + 12))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(mouse_pos):
                    return True # Restart the game
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    return False




def main():
    pygame.init() # Initialise PyGame
    
    # Set up screen/display
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    pygame.display.set_caption("PySnake")
    clock = pygame.time.Clock()

    # Game objects/score
    snake = Snake()
    food = Food()
    score = 0

    # Game settings
    FPS = 60 
    MOVE_SPEED = 7
    frame_count = 0
    running = True

    font = pygame.font.Font(None, 36)
    
    # Game loop
    while running:
        frame_count +=1 # Increments frame counter

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False # If user quits tab, game stops
        
        if snake.check_wall_collision() or snake.check_self_collision():
            print("Game Over!")
            if play_again(screen):  # Call the play_again function
                main()  # Restart the game
            else:
                pygame.quit()
                return
        

        if food.check_snake_collision(snake): # Checks if there is a collision between the snake and the food objects
            print("Collision detected!")
            snake.grow() # Extends the snake by one segment
            food.respawn(snake) # Respawns food at a new position on the grid
            score += 1

        # Handles user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != "DOWN":
            snake.direction = "UP"
        if keys[pygame.K_DOWN] and snake.direction != "UP":
            snake.direction = "DOWN"
        if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
            snake.direction = "LEFT"
        if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
            snake.direction = "RIGHT"

        # Move the snake
        if frame_count % MOVE_SPEED == 0:
            print("Snake is moving")
            snake.move()

        # Draw everything
        screen.fill(BACKGROUND) # A slightly darker beige colour
        drawGrid(screen)
        snake.draw(screen) # Draws the snake onto the screen
        food.draw(screen) # Draws the food object onto screen

        # Score counter
        # Draws a semi-transparent background for the scoreboard
        score_bg_surface = pygame.Surface((120, 40), pygame.SRCALPHA)  # Size: 120x40
        score_bg_surface.fill((50, 50, 50, 150))  # Dark gray with 50% transparency (alpha = 128)
        
        screen.blit(score_bg_surface, (5, 5))  # Draws transparent background at (5, 5)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))  # Draws score text

        clock.tick(FPS) # Controls how many frames per second the game runs at
        pygame.display.flip() # Refreshes screen

    pygame.quit()

if __name__ == "__main__":
    main()