import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
runing = True

screen_w = screen.get_width()
screen_h = screen.get_height()
print(screen_h,screen_w)


bg_image = pygame.image.load(r"C:\\Users\\mateu\Desktop\\Pygame_P\\Ball Pong\\grass.png")


player_pos1 = [10,400]
player_image1 = pygame.image.load(r"C:\\Users\\mateu\Desktop\\Pygame_P\\Ball Pong\\player11.png")
player_speed1 = 10
player_jump_p1 = 0.5
velocity1 = 0
player1_rect = pygame.Rect(player_pos1[0],player_pos1[1],40,40)

player1_w = player_image1.get_width()
player1_h = player_image1.get_height()


player_pos2 = [1760,400]
player_image2 = pygame.image.load(r"C:\\Users\\mateu\Desktop\\Pygame_P\\Ball Pong\\player2.png")
player_speed2 = 10
player_jump_p2 = 0.5
velocity2 = 0


player2_w = player_image2.get_width()
player2_h = player_image2.get_height()


ball = pygame.image.load(r"C:\\Users\\mateu\Desktop\\Pygame_P\\Ball Pong\\ball2.png")
ball_pos = [920,490]
ball_rect = pygame.Rect(ball_pos[0],ball_pos[1], 40,40)
ball_speed_x = 5
ball_speed_y = 5




def music():
    pygame.mixer.music.load(r"C:\\Users\\mateu\\Desktop\\Pygame_P\\Ball Pong\\game_music.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def player2m():
    keys2 = pygame.key.get_pressed()

    if keys2[pygame.K_UP]:
        player_pos2[1] -= player_speed2
    elif keys2[pygame.K_DOWN]:                #Sterowanie gracza 2
        player_pos2[1] += player_speed2
    if keys2[pygame.K_LEFT]:
        player_pos2[0] -= player_speed2
    elif keys2[pygame.K_RIGHT]:
        player_pos2[0] += player_speed2
def player1m():
    keys1 = pygame.key.get_pressed()
    
    if keys1[pygame.K_w]:
        player_pos1[1] -= player_speed1
    elif keys1[pygame.K_s]:
         player_pos1[1] += player_speed1
    if keys1[pygame.K_a]:                   #Sterowanie gracza 1 
        player_pos1[0] -= player_speed1
    elif keys1[pygame.K_d]:
        player_pos1[0] += player_speed1


def g_mapa():
    player1_rect.topleft = (player_pos1[0], player_pos1[1])
    player2_rect = pygame.Rect(player_pos2[0], player_pos2[1], 40, 40)
    player2_rect.topleft = (player_pos2[0], player_pos2[1])

    if player_pos1[0] < 0:
        player_pos1[0] = 0
    if player_pos1[0] > screen_w - player1_w:
        player_pos1[0] = screen_w - player1_w       #Granice gracza 1 na wight
                                                    
    
    if player_pos1[1] < 0:
        player_pos1[1] = 0                          #Granice gracza 1 na heigt
    if player_pos1[1] > screen_h - player1_h:
        player_pos1[1] = screen_h - player1_h

    if player_pos2[0] < 0:
        player_pos2[0] = 0                          #Granice gracza 2 na wight
    if player_pos2[0] > screen_w - player2_w:
        player_pos2[0] = screen_w - player2_w
    
    if player_pos2[1] < 0:
        player_pos2[1] = 0                          #Granice gracza 2 na height
    if player_pos2[1] > screen_h - player2_h:
        player_pos2[1] = screen_h - player2_h


    





music()
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    screen.blit(bg_image,(0,0))
    screen.blit(player_image1,(player_pos1[0],player_pos1[1]))
    screen.blit(player_image2,((player_pos2[0]),player_pos2[1]))
    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y
    screen.blit(ball,(ball_pos[0],ball_pos[1]))

    player1m()
    player2m()
    g_mapa()
    if ball_pos[0] < 0 or ball_pos[0] > screen_w - 40:
        ball_speed_x *= -1
    if ball_pos[1] < 0 or ball_pos[1] > screen_h - 40:
        ball_speed_y *= -1
    
    player2_rect = pygame.Rect(player_pos2[0], player_pos2[1], 40, 40)
    if player1_rect.colliderect(ball_rect):
        ball_speed_x *= -1
    if player2_rect.colliderect(ball_rect):
        ball_speed_x *= -1

    ball_rect.topleft = (ball_pos[0], ball_pos[1])
    
    








    pygame.display.flip()
    clock.tick(60)
pygame.quit()
