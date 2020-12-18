import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

ship = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
speed_player = 0

alien = pygame.image.load("Alien.png")
alienX = random.randint(0, 760)
alienY = random.randint(50, 150)
speed_alien_X = 7
speed_alien_y = 40


background = pygame.image.load('Background.png')

bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
speed_bullet_y = 10
bullet_fire = "ready"


def player(x, y):
    screen.blit(ship, (x, y))

def aliens(x, y):
    screen.blit(alien, (x, y))

def fire_bullet(x, y):
    global bullet_fire
    bullet_fire = "fire"
    screen.blit(bullet, (x+16, y+10))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_player = -8
            if event.key == pygame.K_RIGHT:
                speed_player = 8
            
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        
        if event.type == pygame.KEYUP:
            if speed_player == 8 and event.key == pygame.K_RIGHT:
                speed_player = 0
            if speed_player == -8 and event.key == pygame.K_LEFT:
                speed_player = 0

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    playerX += speed_player

    if playerX < -1:
        playerX =-1

    elif playerX > 737:
        playerX = 737

    alienX += speed_alien_X

    if alienX <= 0:
        speed_alien_X = 7
        alienY +=speed_alien_y

    elif alienX > 760:
        speed_alien_X = -7
        alienY +=speed_alien_y

    if bullet_fire == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= speed_bullet_y
    

    player(playerX, playerY)

    aliens(alienX, alienY)

    pygame.display.update()


pygame.quit()