import pygame
import random
import sys
top_pipe=0
bottom_pipe=0

def game_floor():
    screen.blit(floor,(floorX,590))
    screen.blit(floor,(floorX+565 ,590))
    
def check_collision(pipes):
    #collision with pipes 
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            die_sound.play()
            return False

    #check floor and sky is not hit 
    if (bird_rect.top <= 0 or bird_rect.bottom >=600):
        die_sound.play()
        
        return False
    return True     
     
        

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe=pipe_surface.get_rect(midbottom=(1000,random_pipe_pos-300))
    bottom_pipe=pipe_surface.get_rect(midtop=(1000,random_pipe_pos))
    return bottom_pipe ,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=690:
            screen.blit(pipe_surface,pipe) 
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

 #initialize pygame
pygame.init()
clock=pygame.time.Clock()
bird_move=0 
game_sprites={}

gravity=0.25

#Create pygame window
screen=pygame.display.set_mode((565, 690))

#to add an icon and title to the window
pygame.display.set_caption('FLAPPY BIRD')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#load background
background=pygame.image.load('background.png').convert() 
background=pygame.transform.scale2x(background)#to increase the size of the background

#to load the floor
floor=pygame.image.load('gamefloor2.png').convert()
floor=pygame.transform.scale2x(floor)
floorX=0 #current position of game floor, which will be recreated with every while loop

#to load player (bird)
bird=pygame.image.load('bird.png').convert_alpha() #we use conver alpha for transparent background images
bird_rect=bird.get_rect(center=(100,345))


#to load message1
message1=pygame.image.load('message1.png').convert_alpha()
message1=pygame.transform.scale2x(message1)
game_over_rect = message1.get_rect(center=(282,345))

#to load the sprites
game_sprites['numbers']=(
pygame.image.load('0.png').convert_alpha(),
pygame.image.load('1.png').convert_alpha(),
pygame.image.load('2.png').convert_alpha(),
pygame.image.load('3.png').convert_alpha(),
pygame.image.load('4.png').convert_alpha(),
pygame.image.load('5.png').convert_alpha(),
pygame.image.load('6.png').convert_alpha(),
pygame.image.load('7.png').convert_alpha(),
pygame.image.load('8.png').convert_alpha(),
pygame.image.load('9.png').convert_alpha() )

#building pipes
pipe_surface=pygame.image.load('tube2.png')
pipe_list=[]
pipe_height =[400,500,600]

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

#background sound of flaps 
flap_sound=pygame.mixer.Sound('sfx_flap.mp3')
die_sound=pygame.mixer.Sound('sfx_die.mp3')

#create infinite while loop (main game) 


game_active=True
isstarted = False
isalive=False
scorectr=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN and (event.type==pygame.K_SPACE or event.key==pygame.K_UP):
            bird_move=0  

        if event.type ==SPAWNPIPE and game_active :
            pipe_list.extend(create_pipe())
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and not isstarted:
                isstarted=True
                isalive=True
        if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_SPACE and isstarted and isalive:
                    bird_move=0
                    bird_move-=9
                    flap_sound.play()

    #print(pipe_list)
    screen.blit(background, (0,0))
    if pipe_list!=[]:
        for i in pipe_list:
            if i[0]<-100:
                if pipe_list[pipe_list.index(i)]!=len(pipe_list)-1:
                    if i[0]!=pipe_list[pipe_list.index(i)+1]:
                        scorectr=scorectr+1
                        pipe_list.remove(i)
                    elif i[0]==pipe_list[pipe_list.index(i)+1]:
                        pipe_list.remove(i)
        else:
            print(scorectr,'sc')
            scorectr=int(scorectr/2)
            print(scorectr,'afsc')

             
    if game_active and isstarted==True :


        bird_move+=gravity
        bird_rect.centery +=bird_move #to detect any collision around the bird
    

        #draw pipes
        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)

         #check for collision
        game_active=check_collision(pipe_list )
        isalive=game_active
    else:
        screen.blit(message1,game_over_rect)
        bird_rect.center=(100,345)#to detect any collision around the bird
        bird_move=0
        pipe_list.clear()
        game_activate=True
    screen.blit(bird,bird_rect)
    


    #create floor
    floorX -= 1
    game_floor()
    if floorX<=-565:#if the value of the x coordinate of the floor becomes less than 565 (which is the width of the game window) x coordinate becomes 0
        floorX=0#let it become 0 (stop the loop) if the x coordinate is becomes less than the width of the window (which is not possible), thus, creates an infinite loop
  
    pygame.display.update()
    clock.tick(100 )   