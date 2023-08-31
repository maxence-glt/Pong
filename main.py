import pygame
import random
import math # import cProfile, re

from sys import exit



#TODO: Make ball slower on startup
#TODO: Work on calling class methods instead of calling class attributes and updating them in While loop (more abstraction)
#TODO: Work on computer player



# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("logo.png"))
game_active = False


# Paddles setup
class Paddle:
    speed = 0

    def __init__(self, name, dist):
        self.dist = dist
        self.rect =  pygame.Rect(self.dist, (height / 2) - 41, 10, 82)
        self.score = 0
        self.name = name

        if name == "Player": 
            self.up_K = pygame.K_w
            self.down_K = pygame.K_s
        elif name == "Opponent":
            self.up_K = pygame.K_UP
            self.down_K = pygame.K_DOWN    

    def limits(self):
        if self.rect.top <= 0: self.rect.top = 0
        elif self.rect.bottom >= height: self.rect.bottom = height
    
    def input(self):
        if event.type == pygame.KEYDOWN:
            if event.key == self.up_K: self.speed -= 11
            if event.key == self.down_K: self.speed += 11
        if event.type == pygame.KEYUP:
            if event.key == self.up_K: self.speed += 11
            if event.key == self.down_K: self.speed -= 11
    

class Ball:

    def __init__(self):
        self.rect = pygame.Rect(width/2, height /2, 20, 20)

    def init(self):
        self.rect.x, self.rect.y = width / 2 - 10, height / 2 - 10
        start, start_x, start_y = random.randint(-1, 0), random.randint(7, 9), random.randint(1, 4)
        if start == 0: start += 1
        self.speed_x = (25 * (start_x / 10)) * start
        self.speed_y = (10 * (start_y / 10)) * start
        self.speed_x_original = self.speed_x

    def limit(self):
        if ball.rect.x <= -15: 
            opponent.score += 1
            ball.init()
        if ball.rect.x >= width + 15:
            player.score += 1
            ball.init()
        if ball.rect.y <= 0 or ball.rect.y >= height: self.speed_y = self.speed_y * -1

    def collide(self):
        player_location = (((abs ((player.rect.top - (ball.rect.y + 10)) - 9)) * math.pi) / 100)  # 0 (top) -> 50 -> 100 (bottom) ** OLD
        opponent_location = (((abs ((opponent.rect.top - (ball.rect.y + 10)) - 9)) * math.pi) / 100)   # 0 (top) -> 1.57079 -> 3.14159 (bottom) ** NEW

        if self.rect.colliderect(player.rect):
            self.speed_y = 0
            self.speed_x = (abs (self.speed_x_original * random.uniform(0.8, 1.3)))
            self.speed_y += (round (math.cos(player_location) * 10, 4)) *-1

        if self.rect.colliderect(opponent.rect):
            self.speed_y = 0
            self.speed_x = (abs (self.speed_x_original * random.uniform(0.8, 1.3))) * -1
            self.speed_y += (round (math.cos(opponent_location) * 10, 4)) *-1





def menu(score, side):
    global game_active
    screen.fill((0,0,0))
    screen.blit(title_font.render("Pong", False, "White"), (width / 2 - 80, 40))
    screen.blit(menu_font.render("Press 1 to play with 2 people", False, "White"), (20, (height / 5)))
    screen.blit(menu_font.render("Press 2 to play against computer", False, "White"), (20, height / 3))
    game_active = False
    if side == None and total > 0:      # PyGame has a bug where player.name is passed in as None, thus I needed to reassign None, and make sure it wont popup once you start playing :/
        screen.blit(menu_font.render(f'Player reached {player.score} points and won', False, ("White")), (20, height - 400))
    if score == 0: pass
    else: screen.blit(menu_font.render(f'Opponent reached {opponent.score} points and won', False, ("White")), (20, height - 400))




player = Paddle("Player", 10)
opponent = Paddle("Opponent", (width - 10))
ball = Ball()
title_font = pygame.font.Font("Pixeltype.ttf", 120)
menu_font = pygame.font.Font("bit5x3.ttf", 60)
score_font = pygame.font.Font("bit5x3.ttf", 80)
total = 0




while True:
    screen.fill((0, 0, 0))
    print(player.score, opponent.score)
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            player.input()
            opponent.input()   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                game_active = False
                total += 1
        if game_active == False and event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            ball.init()
            player.score, opponent.score = 0, 0
            player = Paddle("Player", 10)
            opponent = Paddle("Opponent", (width - 10))
            game_active = True
        
        

    if game_active:
        player.rect.y += player.speed
        opponent.rect.y += opponent.speed
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y


        # Control
        player.limits()
        opponent.limits()
        ball.limit()
        ball.collide()

        # Draw
        pygame.draw.rect(screen, "White", player.rect)
        pygame.draw.rect(screen, "White", opponent.rect)
        pygame.draw.ellipse(screen, "White", ball.rect)
        pygame.draw.aaline(screen, "White", (width / 2, 0),(width / 2, height))

        screen.blit(score_font.render(f"{player.score}", False, "White"), ((width / 2) - 120, 50))
        screen.blit(score_font.render(f"{opponent.score}", False, "White"), ((width / 2) + 100, 50))

        if player.score == 10 or opponent.score == 10: 
            game_active = False


    

    else:
        if player.score > opponent.score: 
            screen.fill((0,0,0))
            screen.blit(title_font.render("Pong", False, "White"), (width / 2 - 80, 40))
            screen.blit(menu_font.render("Press 1 to play with 2 people", False, "White"), (20, (height / 5)))
            screen.blit(menu_font.render("Press 2 to play against computer", False, "White"), (20, height / 3))
            menu(player.score, player.name)
        if opponent.score > player.score: 
            screen.fill((0,0,0))
            screen.blit(title_font.render("Pong", False, "White"), (width / 2 - 80, 40))
            screen.blit(menu_font.render("Press 1 to play with 2 people", False, "White"), (20, (height / 5)))
            screen.blit(menu_font.render("Press 2 to play against computer", False, "White"), (20, height / 3))
            menu(opponent.score, opponent.name)
        else: menu(0, None)


    pygame.display.update()
    pygame.time.Clock().tick(60)