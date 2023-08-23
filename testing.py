import pygame
from sys import exit
import random




# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


# Paddles setup
class Paddle:
    racket_height = 140
    speed = 0

    def __init__(self, right_left, dist):
        self.name = right_left
        self.dist = dist
        if right_left == "player": 
            self.up_K = pygame.K_w
            self.down_K = pygame.K_s
        elif right_left == "opponent":
            self.up_K = pygame.K_UP
            self.down_K = pygame.K_DOWN
    
    def rects(self):
        pygame.Rect(self.dist, (height / 2) - 70, 10, 140)

    def limits(self, top, bottom):
        print(top, bottom)
        if top <= 0: top = 0
        elif bottom >= height: bottom = height

    def input(self):
        if event.type == pygame.KEYDOWN:
            if event.key == self.up_K: self.speed -= 7
            if event.key == self.down_K: self.speed += 7
        if event.type == pygame.KEYUP:
            if event.key == self.up_K: self.speed += 7
            if event.key == self.down_K: self.speed -= 7


player = Paddle("player", 10)
# player_rect = player.rects
player_rect = pygame.Rect(10, (height / 2) - 70, 10, 140)

opponent = Paddle("opponent", (width - 10))
# opponent_rect = opponent.rects
opponent_rect = pygame.Rect((width - 10), (height / 2) - 70, 10, 140)





# Ball
ball_rect = pygame.Rect(width/2, height /2, 20, 20)
ball_speed_x = 0
ball_speed_y = 0

# def ball_movement():
#     global ball_speed_x, ball_speed_y
#     player_location = (player_rect.y + 70) - (ball_rect.y + 10)     # 0 -> 660
#     opponent_location = (opponent_rect.y + 70) - (ball_rect.y + 10)
#     print(player_rect.y, opponent_rect.y, player_location, opponent_location)
#     if ball_rect.colliderect(player_rect):
#         if player_location in range(-15, 16): ball_speed_y = 0
#         elif player_location < -15: 
#             ball_speed_y = 0
#             ball_speed_y += 10
#         elif player_location > 16: 
#             ball_speed_y = 0
#             ball_speed_y -= 10
#         ball_speed_x = ball_speed_x * -1
#     if ball_rect.colliderect(opponent_rect): 
#         if opponent_location in range(-15, 16): ball_speed_y = 0
#         elif opponent_location < -15: 
#             ball_speed_y = 0
#             ball_speed_y += 10
#         elif opponent_location > 16: 
#             ball_speed_y = 0
#             ball_speed_y -= 10
#         ball_speed_x = ball_speed_x * -1
#     ball_rect.x += ball_speed_x
#     ball_rect.y += ball_speed_y

# def ball_limits():
#     global opponent_score, player_score, ball_speed_y
#     if ball_rect.x <= -10: 
#         opponent_score += 1
#         ball_init()
#     if ball_rect.x >= width + 10:
#         player_score += 1
#         ball_init()
#     if ball_rect.y == 0: ball_speed_y = ball_speed_y * -1
#     if ball_rect.y == height: ball_speed_y = ball_speed_y * -1

# def ball_init():
    # global ball_speed_x, ball_speed_y
    # ball_speed_x, ball_speed_y = 0, 0
    # ball_rect.x = width / 2 - 10
    # ball_rect.y = height / 2 - 10
    # start = random.randint(0, 1)
    # if start == 0: ball_speed_x -= 15
    # if start == 1: ball_speed_x += 15
    



# Score
player_score = 0
opponent_score = 0
score_font = pygame.font.Font("bit5x3.ttf", 80)




# Game loop
# ball_init()

while True:
   

    # Event loop
    for event in pygame.event.get():
        # X out of the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player.input()
        opponent.input()





    # Update
    screen.fill((0, 0, 0))

    # ball_movement()

    player_rect.y += player.speed
    opponent_rect.y += opponent.speed



    # Control
    player.limits(player_rect.top, player_rect.bottom)
    opponent.limits(opponent_rect.top, opponent_rect.bottom)

    # ball_limits()

    # Draw
    pygame.draw.rect(screen, "White", player_rect)
    pygame.draw.rect(screen, "White", opponent_rect)
    # pygame.draw.ellipse(screen, "White", ball_rect)
    pygame.draw.aaline(screen, "White", (width / 2, 0),(width / 2, height))

    screen.blit(score_font.render(f"{player_score}", False, "White"), ((width / 2) - 120, 50))
    screen.blit(score_font.render(f"{opponent_score}", False, "White"), ((width / 2) + 100, 50))




    pygame.display.update()
    pygame.time.Clock().tick(60)