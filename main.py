#мы не смогли сделать с ботом так что сделали с двумя игроками с клавиатуры
#игрок один w-вверх s-вниз
#игрок 2 на стрелочках
import pygame
import time



pygame.init()
icon = pygame.image.load("1.jpg")
pygame.display.set_icon(icon)
display_width = 1200
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ping pong pisia popa")
clock = pygame.time.Clock()

def rec(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def ball(x, y, rad, color):
    pygame.draw.circle(gameDisplay, color, [x, y], rad)

def TextObjects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def MessegeDisplay(text, size, y):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = TextObjects(text, largeText)
    TextRect.center = (600, y)
    gameDisplay.blit(TextSurf, TextRect)

    if y == 300:
        pygame.display.update()
        time.sleep(2)

def WinMessege(text):
    MessegeDisplay(str(text) + " WIN!", 100, 300)

def Score():
    MessegeDisplay(str(scoreplayer1) + " : " + str(scoreplayer2), 50, 50)

width = 20
height = 200
recx1 = 100
recy1 = 200
recx2 = 1100
recy2 = 200

y1changer = 0
y2changer = 0

radb = 20
ballx = int(display_width/2)
bally = int(display_height/2)
color = (255, 255, 255)

vectorx = 10
vectory = 10

scoreplayer1 = 0
scoreplayer2 = 0

crashed = True

while crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False

        #игрок 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y2changer = -10
            elif event.key == pygame.K_DOWN:
                y2changer = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y2changer = 0

        #игрок 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1changer = -10
            elif event.key == pygame.K_s:
                y1changer = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y1changer = 0

        #print(event)

    if recy1 < 0:
        recy1 = 0
    elif recy1 > 400:
        recy1 = 400

    if recy2 < 0:
        recy2 = 0
    elif recy2 > 400:
        recy2 = 400

    recy1 += y1changer
    recy2 += y2changer

    if bally < 20 or bally > 580:
        vectory = -vectory


    if ballx > recx2 -  20 and not ballx > recx2 and bally > recy2 and bally < recy2 + 200:
        vectorx = -vectorx
    elif ballx < recx1 + 40 and not ballx < recx1 and bally > recy1 and bally < recy1 + 200:
        vectorx = -vectorx


    if ballx > display_width:
        scoreplayer1 += 1
        ballx = int(display_width/2)
        bally = int(display_height/2)

    if ballx < 0:
        scoreplayer2 += 1
        ballx = int(display_width/2)
        bally = int(display_height/2)

    ballx += vectorx
    bally += vectory

    gameDisplay.fill((0, 0, 0))
    rec(recx1, recy1, width, height, (255, 255, 255))
    rec(recx2, recy2, width, height, (255, 255, 255))
    Score()
    if scoreplayer1 >= 3:
        color = (0, 0, 0)
        WinMessege("Player1")
        crashed = False
    elif scoreplayer2 >= 3:
        color = (0, 0, 0)
        WinMessege("Player2")
        crashed = False
    ball(ballx, bally, radb, color)

    pygame.display.update()
    clock.tick(60)