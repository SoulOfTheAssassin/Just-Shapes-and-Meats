import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Zoom and Fade Effect')
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Variables for zoom and fade (now global so they persist between frames)
zoom_factor = 1.0  # Starting zoom factor
fade_alpha = 0  # Starting fade (fully transparent, so the screen is visible)
zoom_speed = 0.05  # Speed of zoom in/out
fade_speed = 5  # Speed of fading to black

# Function to draw a circle on the screen
def draw_circle():
    pygame.draw.circle(screen, RED, (400, 400), 100)

# Function for zoom and fade effect
def zoom_and_fade_effect():
    global zoom_factor, fade_alpha

    # Surface to render game elements
    surface = pygame.Surface((800, 800))

    # Clear the surface before drawing
    surface.fill(WHITE)  # Start with a white background

    # Draw a red circle on the surface
    draw_circle()

    # Zoom effect - scaling the surface
    zoomed_surface = pygame.transform.scale(surface, 
                                            (int(800 * zoom_factor), int(800 * zoom_factor)))
    zoomed_rect = zoomed_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Fade effect - create a surface with alpha transparency (start fully transparent, increase alpha)
    fade_surface = pygame.Surface((800, 800))
    fade_surface.fill((0, 0, 0))  # Black fade
    fade_surface.set_alpha(fade_alpha)  # Apply the alpha transparency

    # Draw zoomed and faded surface on screen
    screen.blit(zoomed_surface, zoomed_rect)
    screen.blit(fade_surface, (0, 0))  # Draw the fading black overlay

    # Update zoom and fade values
    zoom_factor += zoom_speed
    fade_alpha += fade_speed  # Increase the alpha to make the screen fade to black
    if fade_alpha > 255:
        fade_alpha = 255  # Stop increasing alpha once the screen is fully black

    if zoom_factor > 1.5:  # Stop zooming in after a point
        zoom_factor = 1.5

# Main loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white before each frame

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call the zoom and fade effect function continuously
    zoom_and_fade_effect()

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
sys.exit()
