import pygame
from sys import exit


pygame.init()
screen =pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)   #(font type,font size)


#images
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("My game",False,(64,64,64))   #(text,aliase,color64R64G64B=gray)
score_rect = score_surf.get_rect(center = (400,50))


snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))  # snail_x_pos = 600

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #矩形
player_gravity = 0

#set screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#set mouseup           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("jump")
                # player_gravity = -20

            
#import images
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,"#c0e8ec",score_rect)
    pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
    screen.blit(score_surf,score_rect)

    #snail move
    # snail_x_pos -= 4
    # if snail_x_pos < -100 :snail_x_pos = 800
    # screen.blit(snail_surf,(snail_x_pos,250))
    
    
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800    #螢幕寬預設800
    screen.blit(snail_surf,snail_rect)
    

    #Player
    # player_gravity += 1 
    # player_rect.y += player_gravity
    screen.blit(player_surf,player_rect)
    
 
#update 更新
    pygame.display.update()
    clock.tick(60)






