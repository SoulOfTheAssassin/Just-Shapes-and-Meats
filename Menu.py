import pygame
from Cross import *

def create_blurred_background():
    """Capture and blur the current screen, cache the result."""
    global blurred_background
    if blurred_background is None:  # Create only once
        surface = pygame.display.get_surface()
        # Downscale for blur (adjust factor for blur intensity)
        small_surface = pygame.transform.smoothscale(surface, (screen.get_width() // 5, screen.get_height() // 5))
        blurred_background = pygame.transform.smoothscale(small_surface, surface.get_size())

def draw_menu():
    """Draw the blurred menu screen."""
    if blurred_background:
        screen.blit(blurred_background, (0, 0))
    # Overlay text using the custom font
    title_text = Font.title.render("Main Menu", True, "white")
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 200))

    subtitle_text = Font.subtitle.render("Press Enter to Resume", True, "white")
    screen.blit(subtitle_text, (screen.get_width() // 2 - subtitle_text.get_width() // 2, 400))

    name_text = Font.name.render("Just Souls and Prawns", True, 'white')
    me_text = Font.name.render('Oliver Liu', True, 'white')
    screen.blit(name_text, (screen.get_width() // 2 - name_text.get_width() // 2, 50))
    screen.blit(me_text, (screen.get_width() // 2 - me_text.get_width() // 2, 600))

def draw_help_menu():
    """Draw the blurred menu screen."""
    if blurred_background:
        screen.blit(blurred_background, (0, 0))
    # Overlay text using the custom font
    title_text = Font.title.render("Help Menu", True, "white")
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 200))

    subtitle_text = Font.subtitle.render("Use WASD to move Use spacebar to dash", True, "white")
    screen.blit(subtitle_text, (screen.get_width() // 2 - subtitle_text.get_width() // 2, 400))

    name_text = Font.name.render("Just Souls and Prawns", True, 'white')
    me_text = Font.name.render('Oliver Liu', True, 'white')
    screen.blit(name_text, (screen.get_width() // 2 - name_text.get_width() // 2, 50))
    screen.blit(me_text, (screen.get_width() // 2 - me_text.get_width() // 2, 600))

def draw_death_menu():
    """Draw the 'You Died' screen."""
    if blurred_background:
        screen.blit(blurred_background, (0, 0))
    title_text = Font.title.render("YOU DIED", True, "red")
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 200))

    subtitle_text = Font.subtitle.render("Press Enter to Respawn", True, "white")
    screen.blit(subtitle_text, (screen.get_width() // 2 - subtitle_text.get_width() // 2, 400))

