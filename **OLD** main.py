import pygame
from sys import exit
import random




# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")





# Variables
player_speed = 0
opponent_speed = 0




# Player setup
racket_height = 140
x, y = 70, 330
player_speed = 0
player_rect = pygame.Rect(30, (height / 2) - 70, 10, racket_height)

def player_limits():
    if player_rect.top <= 0:
        player_rect.top = 0
    elif player_rect.bottom >= height:
        player_rect.bottom = height





# Opponent setup
opponent_rect = pygame.Rect(width - 30, (height / 2) - 70, 10, racket_height)

def opponent_limits():
    if opponent_rect.top <= 0:
        opponent_rect.top = 0
    elif opponent_rect.bottom >= height:
        opponent_rect.bottom = height




# Ball
ball_rect = pygame.Rect(width/2, height /2, 20, 20)
ball_speed_x = 0
ball_speed_y = 0

def ball_movement():
    global ball_speed_x, ball_speed_y
    player_location = (player_rect.y + 70) - (ball_rect.y + 10)     # 0 -> 660
    opponent_location = (opponent_rect.y + 70) - (ball_rect.y + 10)
    if ball_rect.colliderect(player_rect):
        if player_location in range(-15, 16): ball_speed_y = 0
        elif player_location < -15: 
            ball_speed_y = 0
            ball_speed_y += 10
        elif player_location > 16: 
            ball_speed_y = 0
            ball_speed_y -= 10
        ball_speed_x = ball_speed_x * -1
    if ball_rect.colliderect(opponent_rect): 
        if opponent_location in range(-15, 16): ball_speed_y = 0
        elif opponent_location < -15: 
            ball_speed_y = 0
            ball_speed_y += 10
        elif opponent_location > 16: 
            ball_speed_y = 0
            ball_speed_y -= 10
        ball_speed_x = ball_speed_x * -1
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

def ball_limits():
    global opponent_score, player_score, ball_speed_y
    if ball_rect.x <= -10: 
        opponent_score += 1
        ball_init()
    if ball_rect.x >= width + 10:
        player_score += 1
        ball_init()
    if ball_rect.y == 0: ball_speed_y = ball_speed_y * -1
    if ball_rect.y == height: ball_speed_y = ball_speed_y * -1

def ball_init():
    global ball_speed_x, ball_speed_y
    ball_speed_x, ball_speed_y = 0, 0
    ball_rect.x = width / 2 - 10
    ball_rect.y = height / 2 - 10
    start = random.randint(0, 1)
    if start == 0: ball_speed_x -= 15
    if start == 1: ball_speed_x += 15
    



# Score
player_score = 0
opponent_score = 0
score_font = pygame.font.Font("bit5x3.ttf", 80)




# Game loop
ball_init()

while True:
   

    # Event loop
    for event in pygame.event.get():
        # X out of the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




        # Opponent Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                opponent_speed -= 7
            if event.key == pygame.K_DOWN:
                opponent_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                opponent_speed += 7
            if event.key == pygame.K_DOWN:
                opponent_speed -= 7


        # Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 7
            if event.key == pygame.K_s:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7

    # Update
    screen.fill((0, 0, 0))

    ball_movement()

    player_rect.y += player_speed
    opponent_rect.y += opponent_speed



    # Control
    player_limits()
    opponent_limits()
    ball_limits()


    # Draw
    pygame.draw.rect(screen, "White", player_rect)
    pygame.draw.rect(screen, "White", opponent_rect)
    pygame.draw.ellipse(screen, "White", ball_rect)
    pygame.draw.aaline(screen, "White", (width / 2, 0),(width / 2, height))

    screen.blit(score_font.render(f"{player_score}", False, "White"), ((width / 2) - 120, 50))
    screen.blit(score_font.render(f"{opponent_score}", False, "White"), ((width / 2) + 100, 50))




    pygame.display.update()
    pygame.time.Clock().tick(60)