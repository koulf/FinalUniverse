import pygame
import sys
import star
import random
import math
import os
import ctypes



# Important constants ------------------------------------------------------------------------------------------------
planetarySystems = 1_000

gridSize = 200

starTemplates = {'blue': [], 'white': [], 'yellow': [], 'orange': [], 'red': []}
stars =[]


user32 = ctypes.windll.user32
SW, SH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screenWidth = SW
screenHeight = SH
screenCenter = (screenWidth // 2, screenHeight // 2)

backgroundColor = (0, 0, 0)
green = (0, 127, 0)

GameStopped = False
fullScreen = True
resizing = False

rePainting = False
displacements = []

grid = False

clickables =[]
clicked = []
hovered = []

displayables = []

counter = 0



# Pygame setup ------------------------------------------------------------------------------------------------
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SW // 2 - screenCenter[0], SH // 2 - screenCenter[1])

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Universe')
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('./assets/icon.png'), (32, 32)))



# Diverse functions ------------------------------------------------------------------------------------------------
def initializeCoordinates(stars):
    points = [[0, 0]]
    lineSize = 1
    limit = len(stars)
    while len(points) < limit:
        for direction in range(4):
            if len(points) == limit:
                break
            for iteration in range(lineSize):
                if len(points) == limit:
                    break
                current = list(points[len(points) - 1])
                if direction == 0:
                    current[0] += 1
                    points.append(current)
                elif direction == 1:
                    current[1] -= 1
                    points.append(current)
                elif direction == 2:
                    current[0] -= 1
                    points.append(current)
                else:
                    current[1] += 1
                    points.append(current)
            if direction == 1 or direction == 3:
                lineSize += 1

    locatedStars = []
    p = 0
    for star in stars:
        star.coordinates = [points[p][0] * gridSize + (screenCenter[0] - random.randrange(gridSize * 0.2, gridSize * 0.8 - star.size)), points[p][1] * gridSize + (screenCenter[1] - random.randrange(gridSize * 0.2, gridSize * 0.8 - star.size))] 
        if star.coordinates[0] <= (screenWidth - star.size * 0.5) and star.coordinates[0] >= (0 - star.size * 0.5) and star.coordinates[1] <= (screenHeight - star.size * 0.5) and star.coordinates[1] >= (0 - star.size * 0.5):
            clickables.append(pygame.Rect(star.coordinates[0], star.coordinates[1], star.size, star.size))
            displayables.append(star)
        locatedStars.append(star)
        p += 1

    return locatedStars

def loadStarTemplates():

    for i in range(4):
        starTemplates['blue'].append(pygame.image.load('./assets/stars/main_sequence/star_blue0' + str(i + 1) + '.png'))

    for i in range(4):
        starTemplates['white'].append(pygame.image.load('./assets/stars/main_sequence/star_white0' + str(i + 1) + '.png'))

    for i in range(4):
        starTemplates['yellow'].append(pygame.image.load('./assets/stars/main_sequence/star_yellow0' + str(i + 1) + '.png'))
    
    for i in range(4):
        starTemplates['orange'].append(pygame.image.load('./assets/stars/main_sequence/star_orange0' + str(i + 1) + '.png'))

    for i in range(4):
        starTemplates['red'].append(pygame.image.load('./assets/stars/main_sequence/star_red0' + str(i + 1) + '.png'))

def onHover():
    global hovered
    for clickable in clickables:
        if clickable.collidepoint(pygame.mouse.get_pos()):
            hovered = clickable
            return True
    return False

def onClick():
    if onHover():
        clicked.append(hovered)

def reSituate():
    global rePainting, counter, resizing
    if resizing:
        displacements.clear()
        displacements.append((SW//2 - 800//2) * 10 if not fullScreen else (800//2 - SW//2) * 10)
        displacements.append((SH//2 - 600//2) * 10 if not fullScreen else (600//2 - SH//2) * 10)
        resizing = False
    elif not rePainting:
        area = clicked.pop()
        displacements.clear()
        displacements.append(area.left - screenCenter[0] + area.width // 2)
        displacements.append(area.top - screenCenter[1] + area.height // 2)
        rePainting = True
        counter = 0
    if counter == 9:
        rePainting = False

    clickables.clear()
    displayables.clear()
    for star in stars:
        if rePainting:
            star.coordinates = [star.coordinates[0] - displacements[0] / 10, star.coordinates[1] - displacements[1] / 10]
        else:
            star.coordinates = [round(star.coordinates[0] - displacements[0] / 10), round(star.coordinates[1] - displacements[1] / 10)]
        if star.coordinates[0] <= (screenWidth - star.size * 0.5) and star.coordinates[0] >= (0 - star.size * 0.5) and star.coordinates[1] <= (screenHeight - star.size * 0.5) and star.coordinates[1] >= (0 - star.size * 0.5):
            clickables.append(pygame.Rect(star.coordinates[0], star.coordinates[1], star.size, star.size))
            displayables.append(star)
    counter += 1

def resizeScreen(width, height): 
    global screenWidth, screenHeight, screen, screenCenter, resizing
    resizing = True
    screenWidth = width
    screenHeight = height
    screenCenter = (screenWidth // 2, screenHeight // 2)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SW // 2 - screenCenter[0], SH // 2 - screenCenter[1])
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    reSituate()

def visualizeSystem():
    x



# Main execution ------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    loadStarTemplates()

    for i in range(planetarySystems):
        stars.append(star.star(list(starTemplates.keys())[random.randrange(len(starTemplates))]))

    stars = initializeCoordinates(stars)

    starIterator = 0

    while not GameStopped:
        if rePainting:
            reSituate()

        if starIterator == 4:
            starIterator = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (pygame.key.get_mods() & pygame.KMOD_LALT and event.key == pygame.K_F4):
                sys.exit()

            if (event.type == pygame.MOUSEBUTTONUP and onHover()) or rePainting:
                if visualizeSystem():
                    print("visualize")
                else:
                    if not rePainting:
                        onClick()
                    reSituate()

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_mods() & pygame.KMOD_LALT:
                    if event.key == pygame.K_g:
                        grid = not grid
                    elif event.key == pygame.K_RETURN:
                        fullScreen = not fullScreen
                        r = [SW, SH] if fullScreen else [800, 600]
                        resizeScreen(r[0], r[1])


        screen.fill(backgroundColor)

        for star in displayables:
            image = pygame.transform.scale(starTemplates[star.type][starIterator], (star.size, star.size))
            screen.blit(image, star.coordinates)

        if onHover() and not rePainting:
            pygame.mouse.set_cursor(*pygame.cursors.tri_right)
        # pygame.draw.circle(screen, (255, 255, 255), planetCoordenates, 50)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)


        if grid:
            pygame.draw.line(screen, green, (0, screenCenter[1]), (screenWidth, screenCenter[1]))
            pygame.draw.line(screen, green, (screenCenter[0], 0), (screenCenter[0], screenHeight))

        pygame.time.delay(300)

        pygame.display.update()

        starIterator += 1
