import pygame as pg
import random
from math import sqrt
from pygame import mixer

pg.init()
pg.mixer.init()


screen = pg.display.set_mode((800, 600))

pg.display.set_caption("Space Invaders")

icon = pg.image.load("logo.png")
pg.display.set_icon(icon)

ship = pg.image.load("spaceship.png")
playerX = 370
playerY = 480
speed_player = 0

sound_on = pg.image.load("sound.png")
sound_off = pg.image.load("no_sound.png")
sound = ""


alien = []
alienX = []
alienY = []
speed_alien_X = []
speed_alien_y = []
num_of_enemies = 6

for i in range(num_of_enemies):
    alien.append(pg.image.load("Alien.png"))
    alienX.append(random.randint(0, 760))
    alienY.append(random.randint(50, 150))
    speed_alien_X.append(1.5)
    speed_alien_y.append(40)


background = pg.image.load('Background.jpg')


bullet = pg.image.load("bullet.png")
bulletX = 0
bulletY = 480
speed_bullet_y = 5
bullet_fire = "ready"

score_value = 0
font = pg.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over = pg.font.Font("freesansbold.ttf", 64)

def player(x, y):
    screen.blit(ship, (x, y))

def aliens(x, y, i):
    screen.blit(alien[i], (x, y))

def fire_bullet(x, y):
    global bullet_fire
    bullet_fire = "fire"
    screen.blit(bullet, (x+16, y+10))

def collide(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt(((enemyX-bulletX)**2)+((enemyY-bulletY)**2))
    if distance <= 27:
        return True

def show_score(x, y):
    score = font.render("Score : "+ str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

def game_over():
    over_text = over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 240))

def sound_img():
    if sound == "":
        screen.blit(sound_on, (750, 5))
    if sound == "on":
        screen.blit(sound_on, (750, 5))
        mixer.music.unpause()
    elif sound == "off":
        mixer.music.pause()
        screen.blit(sound_off, (750, 5))

mixer.music.load("background.wav")
mixer.music.play(-1)

clicked = 1


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            if mouse_position[0] > 750 and mouse_position[0] < 782 and mouse_position[1] > 4 and mouse_position[1] < 37:
                if clicked % 2 == 0:
                    sound = "on"
                else: 
                    sound = "off"
                clicked += 1

        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                speed_player = -2.2
            if event.key == pg.K_RIGHT:
                speed_player = 2.2
            
            if event.key == pg.K_SPACE:
                if bullet_fire == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
                    if sound == "on":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()

        
        if event.type == pg.KEYUP:
            if speed_player == 2.2 and event.key == pg.K_RIGHT:
                speed_player = 0
            if speed_player == -2.2 and event.key == pg.K_LEFT:
                speed_player = 0

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    playerX += speed_player

    if playerX < -1:
        playerX =-1

    elif playerX > 737:
        playerX = 737

    for i in range(num_of_enemies):
        if alienY[i] > 400:
            for j in range(num_of_enemies):
                alienY[j] = 1000
            game_over()
            break

        alienX[i] += speed_alien_X[i]

        if alienX[i] <= 0:
            speed_alien_X[i] = 1.5
            alienY[i] +=speed_alien_y[i]

        elif alienX[i] > 760:
            speed_alien_X[i] = -1.5
            alienY[i] +=speed_alien_y[i]
        
        collision = collide(alienX[i], alienY[i], bulletX, bulletY)

        if collision:
            if sound =="on":
                collision_sound = mixer.Sound("explosion.wav")
                collision_sound.play()
            bulletY = 480
            bullet_fire = "ready"
            score_value +=1
            
            alienX[i] = random.randint(0, 760)
            alienY[i] = random.randint(50, 150)
            
        aliens(alienX[i], alienY[i], i)


    if bullet_fire == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= speed_bullet_y

        if bulletY < 0:
            bulletY = 480
            bullet_fire = "ready"

        
    sound_img()

    player(playerX, playerY)

    show_score(textX, textY)

    pg.display.update()


pg.quit()