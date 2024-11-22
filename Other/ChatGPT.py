import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JSAB-Like Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Beat settings
beat_size = 40
beat_speed = 5
beat_frequency = 30  # How often new beats spawn

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
beats = []
score = 0
running = True

# Font
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

def draw_beats(beats):
    for beat in beats:
        pygame.draw.circle(screen, RED, (beat[0], beat[1]), beat_size)

def handle_beats(beats):
    global score
    for beat in beats:
        beat[1] += beat_speed  # Move beats downwards
        if beat[1] > HEIGHT:
            beats.remove(beat)
            score += 1  # Increase score when beat leaves the screen
        elif beat[0] in range(player_x, player_x + player_size) and beat[1] in range(player_y, player_y + player_size):
            return False  # Collision detected (game over)
    return True

def spawn_beat():
    x_pos = random.randint(0, WIDTH - beat_size)
    return [x_pos, -beat_size]

# Main game loop
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn new beats
    if random.randint(1, beat_frequency) == 1:
        beats.append(spawn_beat())

    # Update and draw beats
    if not handle_beats(beats):
        # Game over condition
        running = False

    # Draw the player and beats
    draw_player(player_x, player_y)
    draw_beats(beats)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game frame rate
    clock.tick(FPS)

# Game over screen
screen.fill(BLACK)
game_over_text = font.render("Game Over", True, WHITE)
score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()

# Wait for a while before quitting
time.sleep(3)
pygame.quit()
