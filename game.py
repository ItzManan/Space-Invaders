import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

ship = pygame.image.load("spaceship.png")

alien = pygame.image.load("Alien.png")

playerX = 370
playerY = 480
speed_player = 0

alienX = random.randint(0, 760)
alienY = random.randint(50, 150)
speed_alien_X = 0.3
speed_alien_y = 40

def player(x, y):
    screen.blit(ship, (x, y))

def aliens(x, y):
    screen.blit(alien, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_player = -0.5
            if event.key == pygame.K_RIGHT:
                speed_player = 0.5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_player = 0

    screen.fill((0, 0, 0))

    playerX += speed_player

    if playerX < -1:
        playerX =-1

    elif playerX > 737:
        playerX = 737

    alienX += speed_alien_X

    if alienX <= 0:
        speed_alien_X = 0.3
        alienY +=speed_alien_y

    elif alienX > 760:
        speed_alien_X = -0.3
        alienY +=speed_alien_y
    

    player(playerX, playerY)

    aliens(alienX, alienY)

    pygame.display.update()


pygame.quit()