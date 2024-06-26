import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score:{current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
    # print(current_time)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect) #螢幕行進中障礙物
            else:
                screen.blit(fly_surf,obstacle_rect)



        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_rect_list
    else : return []

    
pygame.init()
screen =pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)   #(font type,font size)
game_active = False
start_time = 0
score = 0

#images
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("My game",False,(64,64,64))   #(text,aliase,color64R64G64B=gray)
score_rect = score_surf.get_rect(center = (400,50))

#Obstacles障礙物
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))  # snail_x_pos = 600

fly_surf = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
# fly_rect = fly_surf.get_rect(center = (200,200))

obstacle_rect_list = []

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #矩形
player_gravity = 0

#Intro screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))


game_name = test_font.render("Pixel Runner",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press up to run",False,(111,196,169))
game_message_rect = game_message.get_rect(center =(400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)


#set screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#set mouse
        if game_active:  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
                # snail_rect.left = 800 
                start_time = int(pygame.time.get_ticks()/1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100) ,300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100) ,210)))
    
    #import images
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,"#c0e8ec",score_rect)
        # pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        #Player
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0

        screen.blit(player_surf,player_rect)

    #obstacle 障礙  movement 
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    #collision碰撞snail exit game
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message = test_font.render(f"Your score: {score}", False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,320))
        screen.blit(game_name,game_name_rect)

#gameover screen score        
        if score == 0:
            screen.blit(game_message, game_message_rect)

        else :
            screen.blit(score_message,score_message_rect)


#update 更新
    pygame.display.update()
    clock.tick(60)






