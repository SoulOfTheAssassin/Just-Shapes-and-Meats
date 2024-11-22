# Example file showing a circle moving on screen
import pygame
import sys
sys.dont_write_bytecode = True

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
PLAYER_SPEED = 300
PLAYER_DASH_DISTANCE = 70
dashCooldown = 0
DASH_MAX_COOLDOWN = 70
DASH_LINE_OFFSET = 10
facing = {'x': 0, 'y': 0}

def Dash() -> float:
    neg = -DASH_LINE_OFFSET
    pos = DASH_LINE_OFFSET
    faceX = facing['x']
    faceY = facing['y']
    playerNewXPos = playerPos.x + (PLAYER_DASH_DISTANCE*faceX)
    playerNewYPos = playerPos.y + (PLAYER_DASH_DISTANCE*faceY)
    # if faceX == -1:
    #     if faceY == 1:
    #         offset1 = [neg, neg]
    #         offset2 = [pos, pos]
    #     elif faceY == 0:
    #         offset1 = [0, pos]
    #         offset2 = [0, neg]
    #     elif faceY == -1:
    #         offset1 = [neg, pos]
    #         offset2 = [pos, neg]
    # elif faceX == 0:
    #     if faceY == 1:
    #         offset1 = [neg, 0]
    #         offset2 = [pos, 0]
    #     elif faceY == 0:
    #         offset2 = [0, 0]
    #         offset1 = [0, 0]
    #     elif faceY == -1:
    #         offset1 = [pos, 0]
    #         offset2 = [neg, 0]
    # elif faceX == 1:
    #     if faceY == 1:
    #         offset1 = [neg, pos]
    #         offset2 = [pos, neg]
    #     elif faceY == 0:
    #         offset1 = [0, pos]
    #         offset2 = [0, neg]
    #     elif faceY == -1:
    #         offset1 = [pos, pos]
    #         offset2 = [neg, neg]
            
    #     pygame.draw.line(surface=screen, color='white', width=4, 
    #                      start_pos=(playerPos.x + offset1[0], playerPos.y + offset1[1]),
    #                      end_pos=(playerNewXPos + offset1[0], playerNewYPos + offset1[1]))
    #     pygame.draw.line(surface=screen, color='white', width=10, 
    #                      start_pos=(playerPos.x + offset2[0], playerPos.y + offset2[1]),
    #                      end_pos=(playerNewXPos + offset2[0], playerNewYPos + offset2[1]))
    playerPos.x = playerNewXPos
    playerPos.y = playerNewYPos
    return DASH_MAX_COOLDOWN

playerPos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.draw.rect(screen, 'red', pygame.Rect(10, 10, 20, 20))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    playerRect = pygame.Rect(playerPos[0], playerPos[1], 15, 15)
    pygame.draw.rect(surface=screen, color='cyan', rect=playerRect)
    # pygame.draw.polygon(surface=screen, color="cyan", points=[(playerPos[0]+5, playerPos[1]+5), 
    #                                                           (playerPos[0]+5, playerPos[1]-5), 
    #                                                           (playerPos[0]-5, playerPos[1]-5), 
    #                                                           (playerPos[0]-5, playerPos[1]+5)], width=4)
    if dashCooldown > 0:
        dashCooldown -= 1
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
    if keys[pygame.K_SPACE] and dashCooldown == 0 and facing != {'x': 0, 'y': 0}:
        dashCooldown = Dash()

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()