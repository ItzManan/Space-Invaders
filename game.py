import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
ship = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480 

def player():
    screen.blit(ship, (playerX, playerY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    player()
    pygame.display.update()
pygame.quit()