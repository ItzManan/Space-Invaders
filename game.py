import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
ship = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480 
speed = 0

def player(x, y):
    screen.blit(ship, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -1
            if event.key == pygame.K_RIGHT:
                speed = 1
        
        if event.type == pygame.KEYUP:
            speed = 0

    screen.fill((0, 0, 0))

    playerX += speed
    if playerX < -1:
        playerX =-1
    elif playerX > 737:
        playerX = 737
    player(playerX, playerY)
    pygame.display.update()
pygame.quit()