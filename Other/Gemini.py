import pygame
import random

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game clock
clock = pygame.time.Clock()

# Game variables
score = 0
level = 1
shapes = []

# Shape class
class Shape:
    def __init__(self, shape_type, x, y, speed, color):
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color

    def draw(self):
        if self.shape_type == 'square':
            pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))
        elif self.shape_type == 'circle':
            pygame.draw.circle(screen, self.color, (self.x, self.y), 25)

    def move(self):
        self.y += self.speed

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(BLACK)

    # Generate shapes
    if random.randint(1, 100) < level * 5:
        shape_type = random.choice(['square', 'circle'])
        x = random.randint(0, screen_width - 50)
        y = 0
        speed = random.randint(1, 3)
        color = random.choice([RED, GREEN, BLUE])
        shapes.append(Shape(shape_type, x, y, speed, color))

    # Move and draw shapes
    for shape in shapes:
        shape.move()
        shape.draw()

        # Check for collisions (basic implementation)
        if shape.y > screen_height:
            shapes.remove(shape)
            score -= 10

    # Player input (simplified)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # Move player left
        pass
    elif keys[pygame.K_RIGHT]:
        # Move player right
        pass
    # Draw score and level
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (screen_width - 150, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()