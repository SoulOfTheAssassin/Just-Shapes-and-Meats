import pygame
import sys
import random
from Cross import screen
# from Menu import *

sys.dont_write_bytecode = True

# pygame setup
pygame.init()

pygame.display.set_caption('Just Shapes and Meats - Oliver')
clock = pygame.time.Clock()
running = True
dt = 0
PLAYER_SPEED = 300
PLAYER_DASH_DISTANCE = 100
DASH_MAX_COOLDOWN = 100
facing = {'x': 0, 'y': 0}
enemyColour = (225, 0, 130)

# Define the red square (static object)
red_square = pygame.Rect(20, 20, 20, 20)

class Player(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.sections = [
            pygame.Rect(width // 2, 0, width // 2, height // 2),  # Top-right
            pygame.Rect(width // 2, height // 2, width // 2, height // 2),  # Bottom-right
            pygame.Rect(0, height // 2, width // 2, height // 2),  # Bottom-left
            pygame.Rect(0, 0, width // 2, height // 2),  # Top-left
        ]
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = playerPos
        self.colour = colour
        self.invincible = False
        self.invincible_time = 0
        self.lives = 4
        self.dashCooldown = 0

    def update(self, dt):
        if self.invincible:
            # Check if invincibility has expired
            if pygame.time.get_ticks() - self.invincible_time > 2000:
                self.invincible = False

        # Handle player movement based on key inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            playerPos.y -= PLAYER_SPEED * dt
            facing['y'] = -1
        elif keys[pygame.K_s]:
            playerPos.y += PLAYER_SPEED * dt
            facing['y'] = 1
        else:
            facing['y'] = 0
        if keys[pygame.K_a]:
            playerPos.x -= PLAYER_SPEED * dt
            facing['x'] = -1
        elif keys[pygame.K_d]:
            playerPos.x += PLAYER_SPEED * dt
            facing['x'] = 1
        else:
            facing['x'] = 0

        if self.dashCooldown != 0:
            self.dashCooldown -= 1  # Decrement cooldown every frame

        # Update player rect position
        self.rect.center = playerPos

        # Dash logic
        if keys[pygame.K_SPACE] and self.dashCooldown == 0 and facing != {'x': 0, 'y': 0}:
            self.dash()

    def dash(self):
        self.dashCooldown = DASH_MAX_COOLDOWN

        # Move the player to the new position
        playerPos.x += (PLAYER_DASH_DISTANCE * facing['x'])
        playerPos.y += (PLAYER_DASH_DISTANCE * facing['y'])

    def take_damage(self):
        """Reduce player size and enable invincibility."""
        if not self.invincible and self.lives > 0:
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()
            self.sections.pop(0)  # Remove the next section
            self.lives -= 1

    def draw(self):
        for i, section in enumerate(self.sections):
            offset_rect = section.copy()
            offset_rect.topleft = (self.rect.left + section.x, self.rect.top + section.y)
            pygame.draw.rect(screen, self.colour, offset_rect)

        # Draw invincibility circle if the player is invincible
        if self.invincible:
            pygame.draw.circle(screen, (255, 255, 255), self.rect.center, 20, 2)  # White invincibility circle

    def is_dead(self):
        return self.lives == 0

# Initialize player
playerPos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerSize = 13
player = Player('cyan', playerSize, playerSize)
player.__init__('cyan', playerSize, playerSize)

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction, colour, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.rect = pygame.Rect(x, y, 20, 20)  # Diameter = 20
        self.speed = speed
        self.direction = direction  # (x, y) vector
        self.colour = colour

    def update(self, dt):
        self.rect.x += self.direction[0] * self.speed * dt
        self.rect.y += self.direction[1] * self.speed * dt

    def draw(self):
        pygame.draw.ellipse(screen, self.colour, self.rect)

# Ball management
balls = []
BALL_SPAWN_INTERVAL = 2000  # milliseconds
last_ball_spawn = 0

def spawn_ball():
    """Spawn a ball from a random side of the screen."""
    side = random.choice(['left', 'right', 'top', 'bottom'])
    if side == 'left':
        x, y = 0, random.randint(0, screen.get_height())
        direction = (1, 0)
    elif side == 'right':
        x, y = screen.get_width(), random.randint(0, screen.get_height())
        direction = (-1, 0)
    elif side == 'top':
        x, y = random.randint(0, screen.get_width()), 0
        direction = (0, 1)
    else:  # 'bottom'
        x, y = random.randint(0, screen.get_width()), screen.get_height()
        direction = (0, -1)

    balls.append(Ball(x, y, random.randint(150, 300), direction, enemyColour))

# Menu state
# menuType = 'menu'
menuType = ''
blurred_background = None
prev_menuType = None  # Track the previous menu type

def reset_player():
    """Reset the player's position, lives, and sections."""
    global playerPos, player, balls
    playerPos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player = Player('cyan', 15, 15)
    balls = []  # Clear all balls

# Level System
level = 1
max_levels = 5

def level_up():
    global level, BALL_SPAWN_INTERVAL
    level += 1
    BALL_SPAWN_INTERVAL -= 100  # Increase difficulty by spawning balls faster

def check_level_up():
    if len(balls) == 0 and player.lives == 4:
        level_up()

pygame.draw.rect(screen, enemyColour, red_square)
# Main game loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     # if event.key == pygame.K_RETURN:
        #     #     if menuType != '':
        #     #         menuType = ''
        #     # if event.key == pygame.K_h:
        #     #     if menuType != 'help':
        #     #         menuType = 'help'

    # Update the game state
    screen.fill("black")  # Clear the screen

    # Update player and balls only if not in a menu
    if menuType == '':
        player.update(dt)
        player.draw()

        # Check for death and reset
        if player.is_dead():
            reset_player()
            menuType = ''  # Activate death menu

        # Spawn balls
        if pygame.time.get_ticks() - last_ball_spawn > BALL_SPAWN_INTERVAL:
            spawn_ball()
            last_ball_spawn = pygame.time.get_ticks()

        # Update and draw balls
        for ball in balls:
            ball.update(dt)
            ball.draw()

        # Check for collisions with balls
        for ball in balls:
            if player.rect.colliderect(ball.rect):
                player.take_damage()

        # Check for level up
        check_level_up()

    # # Draw menu or help screen if active
    # if menuType != '':
    #     if menuType == 'menu':
    #         draw_menu()
    #     elif menuType == 'help':
    #         draw_help_menu()
    #     elif menuType == 'dead':
    #         draw_death_menu()

    pygame.display.flip()
    dt = clock.tick(60) / 1000  # Time delta in seconds

pygame.quit()