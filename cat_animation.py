import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('assets/cat.png')
catx = 10
caty = 10
direction = 'right'

cat2Img = pygame.image.load('assets/cat2_stefan.png')
cat2x = 300
cat2y = 210
direction2 = 'up'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    if direction2 == 'up':
        cat2y -= 5
        if cat2y == -30:
            direction2 = 'left'
    elif direction2 == 'left':
        cat2x -= 5
        if cat2x == -30:
            direction2 = 'down'
    elif direction2 == 'down':
        cat2y += 5
        if cat2y == 210:
            direction2 = 'right'
    elif direction2 == 'right':
        cat2x += 5
        if cat2x == 300:
            direction2 = 'up'

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(cat2Img, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)