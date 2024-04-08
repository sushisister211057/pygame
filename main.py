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
text_surface = test_font.render("My game",False,"Black")   #(text,aliase,color)

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# snail_x_pos = 600
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #矩形

#set screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#import images
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    #snail move
    # snail_x_pos -= 4
    # if snail_x_pos < -100 :snail_x_pos = 800
    # screen.blit(snail_surf,(snail_x_pos,250))
    
    
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800    #螢幕寬預設800
    screen.blit(snail_surf,snail_rect)

    #player move
    # player_rect.left += 1
    screen.blit(player_surf,player_rect)
    

#update 更新
    pygame.display.update()
    clock.tick(60)





