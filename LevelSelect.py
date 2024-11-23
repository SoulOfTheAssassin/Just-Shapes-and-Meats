import pygame
import sys
import random
# from Menu import *

sys.dont_write_bytecode = True

icon = pygame.image.load('JustShapesAndMeats.png')
map = pygame.image.load('LevelMapV2.png')

# pygame setup
pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Just Shapes and Meats - Oliver and Sean (Nelson was here)')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
menuRunning = True
dt = 0
playerSpeed = 300
playerDashDistance = 100
dashMaxCooldown = 100
facing = {'x': 0, 'y': 0}
enemyColour = (225, 0, 130)
playing = True
PLAYER_SIZE = (20, 20)

# Level Data
class Level:
    moveNumber = {'Up': 1, 'Left': 2, 'Down': 3, 'Right': 4}
    actionDict = {pygame.K_w: 1, pygame.K_a: 2, pygame.K_s: 3, pygame.K_d: 4}
    statusDict = {1: 'Unlocked', 2: 'Locked', 3: 'Complete'}
    dict = {}
    mapDict = {
        0: (55, 45),
        1: (55, 184),
        2: (203, 184),
        3: (351, 184),
        4: (499, 184),
        5: (55, 324),
        6: (203, 324),
        7: (203, 464),
        8: (499, 464),
        9: (351, 464)
    }
    selected = 0

def Tutorial():
    pass

def Level1():
    pass

def Level2():
    pass

def Level3():
    pass

def Level4():
    pass

def Level5():
    pass

def Level6():
    pass

def Level7():
    pass

def Level8():
    pass

def Bossfight():
    pass

Level.dict = {
    #   Level Number: [Name, Locked/Unlocked, Adjacent Levels, Attempts, Function]
        0: ['Tutorial', 1, [None, None, 1, None], 0, Tutorial],
        1: ['Level 1', 2, [0, None, 5, 2], 0, Level1],
        2: ['Level 2', 2, [None, 1, 6, 3], 0, Level2],
        3: ['Level 3', 2, [None, 2, None, 4], 0, Level3],
        4: ['4', 2, [None, 3, 8, None], 0, Level4],
        5: ['5', 2, [1, None, None, 6], 0, Level5],
        6: ['6', 2, [2, 5, 7, None], 0, Level6],
        7: ['7', 2, [6, None, None, 9], 0, Level7],
        8: ['8', 2, [4, 9, None, None], 0, Level8],
        9: ['BOSSFIGHT', 2, [None, 7, None, 8], 0, Bossfight]
    }
# Functions for UI and Level Selection
def Rectangle(x: float, y: float, width: float, height: float):
    rectX = x - width // 2
    rectY = y - height // 2
    return pygame.Rect(rectX, rectY, width, height)


def DrawLevelDisplay(levelNumber: int):
    fill = Rectangle(screen.get_width() // 2, (screen.get_height() // 2) + 300, 345, 100)
    pygame.draw.rect(screen, 'black', fill)
    button = Rectangle(screen.get_width() // 2, (screen.get_height() // 2) + 300, 350, 105)
    pygame.draw.rect(screen, 'cyan', button, 8)
    title = pygame.font.Font('Fonts\\Title.otf', 18)
    text_surface = title.render(Level.dict[levelNumber][0], True, 'white')
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) + 300))
    screen.blit(text_surface, text_rect)


def UnlockLevel(currentLevel: int):
    for i in Level.dict[currentLevel][3]:
        if i is not None:
            Level.dict[i][1] = 1


def SelectLevel(currentLevel: int, action: int) -> None:
    selectedLevel = Level.dict[currentLevel][2][action - 1]
    if selectedLevel is None:
        selectedLevel = currentLevel
    Level.selected = selectedLevel


# Function to create the "Enter Level" zoom and fade effect, and return when finished
def EnterLevelEffect(screen, fadeSpeed=5):
    """Fades the screen to black.

    Args:
        screen: The Pygame display surface.
        fadeSpeed: The speed of the fade effect (higher values fade faster).
    """

    fadeSurface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    alpha = 0

    while alpha < 255:
        fadeSurface.fill((0, 0, 0, alpha))
        screen.blit(fadeSurface, (0, 0))
        pygame.display.flip()
        alpha += fadeSpeed
        pygame.time.delay(10)
    return False


# Main game loop
while playing:
    while menuRunning:
        keys = pygame.key.get_pressed()  # Get all key states
        screen.blit(map, (0, 0))
        player = pygame.Rect(Level.mapDict[Level.selected], PLAYER_SIZE)
        
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
                    menuRunning = EnterLevelEffect(screen)  # Exit menu after the effect is done
                    gameRunning = True
        
        if menuRunning:  # Only draw the level display if the menu is still running
            DrawLevelDisplay(Level.selected)
            pygame.draw.rect(screen, 'cyan', player)
        
        pygame.display.flip()

    while gameRunning:
        screen.fill('cyan')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
        pygame.display.flip()
pygame.quit()