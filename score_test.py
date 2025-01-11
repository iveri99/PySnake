import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scoreboard Test")
clock = pygame.time.Clock()

# Font settings
font = pygame.font.Font(None, 36)  # Default font, size 36
score = 0  # Example score

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Render and display the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 10))  # Display at (10, 10)

    pygame.display.flip()
    clock.tick(30)  # Limit to 30 FPS

pygame.quit()