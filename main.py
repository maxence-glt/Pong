import pygame
from sys import exit





# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")





# Variables
player_speed = 0
opponent_speed = 0




# Player setup
x, y = 70, 330
player_speed = 0
player_rect = pygame.Rect(10, (height / 2) - 70, 10, 140)

def player_limits():
    if player_rect.top <= 0:
        player_rect.top = 0
    elif player_rect.bottom >= height:
        player_rect.bottom = height





# Opponent setup
opponent_rect = pygame.Rect(width - 20, (height / 2) - 70, 10, 140)

def opponent_limits():
    if opponent_rect.top <= 0:
        opponent_rect.top = 0
    elif opponent_rect.bottom >= height:
        opponent_rect.bottom = height




# Ball
ball_rect = pygame.Rect(width/2 - 10, height /2 - 10, 20, 20)

def ball_limits():
    if ball_rect.x <= 0:
        pygame.quit()
    if ball_rect.x >= width:
        pygame.quit() 





# Score
player_score = 0
opponent_score = 0
score_font = pygame.font.Font("bit5x3.ttf", 80)
pscore = score_font.render(f"{player_score}", False, "White")
oscore = score_font.render(f"{opponent_score}", False, "White")





# Game loop
while True:
    
    # Event loop
    for event in pygame.event.get():
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

    screen.blit(pscore, ((width / 2) - 120, 50))
    screen.blit(oscore, ((width / 2) + 100, 50))




    pygame.display.update()
    pygame.time.Clock().tick(60)