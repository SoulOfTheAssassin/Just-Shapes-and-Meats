import pygame
import sys
import random
from Cross import screen
# from Menu import *

sys.dont_write_bytecode = True

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Just Shapes and Meats - Oliver and Nelson')
clock = pygame.time.Clock()
menuRunning = True
dt = 0
playerSpeed = 300
playerDashDistance = 100
dashMaxCooldown = 100
facing = {'x': 0, 'y': 0}
enemyColour = (225, 0, 130)
playing = True

# Level Data
class Level:
    moveNumber = {'Up': 1, 'Left': 2, 'Down': 3, 'Right': 4}
    actionDict = {pygame.K_w: 1, pygame.K_a: 2, pygame.K_s: 3, pygame.K_d: 4}
    statusDict = {1: 'Unlocked', 2: 'Locked', 3: 'Complete'}
    dict = {
        0: ['Tutorial', 1, [None, None, 1, None], 0],
        1: ['Level 1', 2, [0, None, 5, 2], 0],
        2: ['Level 2', 2, [None, 1, 6, 3], 0],
        3: ['Level 3', 2, [None, 2, None, 4], 0],
        4: ['4', 2, [None, 3, 8, None], 0],
        5: ['5', 2, [1, None, None, 6], 0],
        6: ['6', 2, [2, 5, 7, None], 0],
        7: ['7', 2, [6, None, None, 9], 0],
        8: ['8', 2, [4, 9, None, None], 0],
        9: ['BOSSFIGHT', 2, [None, 7, None, 8], 0]
    }
    selected = 0

def Level1():
    
# Functions for UI and Level Selection
def Rectangle(x: float, y: float, width: float, height: float):
    rectX = x - width // 2
    rectY = y - height // 2
    return pygame.Rect(rectX, rectY, width, height)


def DrawLevelDisplay(levelNumber: int):
    fill = Rectangle(screen.get_width() // 2, (screen.get_height() // 2) + 100, 345, 145)
    pygame.draw.rect(screen, 'black', fill)
    button = Rectangle(screen.get_width() // 2, (screen.get_height() // 2) + 100, 350, 150)
    pygame.draw.rect(screen, 'cyan', button, 8)
    title = pygame.font.Font('Fonts\\Title.otf', 18)
    text_surface = title.render(Level.dict[levelNumber][0], True, 'white')
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) + 45))
    screen.blit(text_surface, text_rect)


def UnlockLevel(currentLevel: int):
    for i in Level.dict[currentLevel][2]:
        if i is not None:
            Level.dict[i][1] = 1


def SelectLevel(currentLevel: int, action: int) -> None:
    selectedLevel = Level.dict[currentLevel][2][action - 1]
    if selectedLevel is None:
        selectedLevel = currentLevel
    Level.selected = selectedLevel


# Function to create the "Enter Level" zoom and fade effect, and return when finished
def EnterLevelEffect():
    zoomFactor = 1.0 
    fadeAlpha = 0 
    zoomSpeed = 0.05
    fadeSpeed = 2  # Slower fade speed to make it more gradual

    surface = pygame.Surface((800, 800))

    while zoomFactor < 1.5 or fadeAlpha < 255:
        # Apply zoom effect
        zoomedSurface = pygame.transform.scale(surface, 
                                                (int(800 * zoomFactor), int(800 * zoomFactor)))
        zoomedRect = zoomedSurface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        # Apply fade effect
        fadeSurface = pygame.Surface((800, 800))
        fadeSurface.fill((0, 0, 0))  # Black fade color
        fadeSurface.set_alpha(fadeAlpha)

        # Draw the zoomed and faded surfaces
        screen.blit(zoomedSurface, zoomedRect)
        screen.blit(fadeSurface, (0, 0))

        # Update zoom and fade values gradually
        zoomFactor += zoomSpeed
        fadeAlpha += fadeSpeed  # Increase fadeAlpha gradually

        # Clamp the values to make sure they don't exceed limits
        if fadeAlpha > 255:
            fadeAlpha = 255
        
        if zoomFactor > 1.5:
            zoomFactor = 1.5

        pygame.display.flip()
        pygame.time.delay(10)  # Delay to allow visual effect to be noticeable

    # After effect finishes, continue with the game or transition to the next stage
    return


# Main game loop
while playing:
    while menuRunning:
        keys = pygame.key.get_pressed()  # Get all key states
        screen.fill('white')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRunning = False
            
            # Check for keydown events and select the level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    SelectLevel(Level.selected, Level.actionDict[pygame.K_w])
                elif event.key == pygame.K_a:
                    SelectLevel(Level.selected, Level.actionDict[pygame.K_a])
                elif event.key == pygame.K_s:
                    SelectLevel(Level.selected, Level.actionDict[pygame.K_s])
                elif event.key == pygame.K_d:
                    SelectLevel(Level.selected, Level.actionDict[pygame.K_d])
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    EnterLevelEffect()
                    menuRunning = False  # Exit menu after the effect is done
        
        if menuRunning:  # Only draw the level display if the menu is still running
            DrawLevelDisplay(Level.selected)
        
        pygame.display.flip()

pygame.quit()