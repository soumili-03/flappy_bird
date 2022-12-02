import pygame

 #initialize pygame
pygame.init()

bird_move=0

gravity=0.15

#Create pygame window
screen=pygame.display.set_mode((565, 690))

#to add an icon and title to the window
pygame.display.set_caption('FLAPPY BIRD')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#load background
background=pygame.image.load('background.png')
background=pygame.transform.scale2x(background)#to increase the size of the background

#to load the floor
floor=pygame.image.load('gamefloor2.png')
floor=pygame.transform.scale2x(floor)
floorX=0#current position of game floor, which will be recreated with every while loop

#to load player (bird)
playerImg=pygame.image.load('bird.png')
bird_rect=playerImg.get_rect(center=(100, 512))

#create infinite while loop (main game)
run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                    bird_move=0
                    bird_move=bird_move-8
                    bird_rect.center=(100, 512)#to detect any collision around the bird

    bird_move=bird_move+gravity
    bird_rect.centery=bird_rect.centery+bird_move#to detect any collision around the bird
    screen.blit(background, (0,0))
    screen.blit(background, (0,0))
    screen.blit(floor, (floorX, 590))#to continuously change the x coordinate of the game floor
    screen.blit(floor, (floorX+565, 590))

    if floorX<=-565:#if the value of the x coordinate of the floor becomes less than 565 (which is the width of the game window) x coordinate becomes 0
        floorX=0#let it become 0 (stop the loop) if the x coordinate is becomes less than the width of the window (which is not possible), thus, creates an infinite loop

    screen.blit(playerImg, bird_rect)

    floorX=floorX-1#updating the x coordinate of the floor
  
    pygame.display.update()