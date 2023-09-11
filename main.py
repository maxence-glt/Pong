import pygame
import random
import math

from sys import exit


# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("static/logo.png"))
game_active = False


# Paddles setup
class Paddle:
    speed = 0

    def __init__(self, name, dist):
        self.dist = dist
        self.rect = pygame.Rect(self.dist, (height / 2) - 41, 10, 82)
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
    speed = 13
    
    def __init__(self):
        self.rect = pygame.Rect(width/2, height /2, 20, 20)

    def init(self):
        self.rect.x, self.rect.y = width / 2 - 10, height / 2 - 10
        start, start_x, start_y = random.randint(-1, 0), random.randint(7, 9), random.randint(1, 4)
        if start == 0: start += 1
        self.speed_x = Ball.speed * start
        self.speed_y = (5 * (start_y / 10)) * start
        self.speed_x_original = (25 * (start_x / 10)) * start

    def limit(self):
        if ball.rect.x <= -15: 
            opponent.score += 1
            ball.init()
        if ball.rect.x >= width + 15:
            player.score += 1
            ball.init()
        if ball.rect.y <= 0 or ball.rect.y >= height: self.speed_y = self.speed_y * -1

    def collide(self):
        player_location = (((abs ((player.rect.top 
                                   - (ball.rect.y + 10)) - 9)) 
                                   * math.pi) 
                                   / 100)  # 0 (top) -> 50 -> 100 (bottom) ** OLD
        opponent_location = (((abs ((opponent.rect.top 
                                     - (ball.rect.y + 10)) - 9)) 
                                     * math.pi) 
                                     / 100)   # 0 (top) -> 1.57079 -> 3.14159 (bottom) ** NEW

        if self.rect.colliderect(player.rect):
            self.speed_y = 0
            self.speed_x = (abs (self.speed_x_original * random.uniform(0.8, 1.3)))
            self.speed_y += (round (math.cos(player_location) * 10, 4)) *-1

        if self.rect.colliderect(opponent.rect):
            self.speed_y = 0
            self.speed_x = (abs (self.speed_x_original * random.uniform(0.8, 1.3))) * -1
            self.speed_y += (round (math.cos(opponent_location) * 10, 4)) *-1

class Computer(Paddle):
    
    def speed(self):
        if ball.rect.x > width * (1/3):
            if ball.rect.y < opponent.rect.y + 30:
                opponent.rect.y += -11

            if ball.rect.y > opponent.rect.y + 50:
                opponent.rect.y += 11

            else:
                opponent.rect.y += 0






def menu(score, side):
    global game_active
    screen.fill((0,0,0))
    screen.blit(title_font.render("Pong", False, "White"), (width / 2 - 80, 40))
    screen.blit(menu_font.render("Press 1 to play with 2 people", False, "White"), (20, (height / 5)))
    screen.blit(menu_font.render("Press 2 to play against computer", False, "White"), (20, height / 3))
    game_active = False
    if side == None and on_off > 0:     # PyGame has a bug where player.name is passed in as None, thus I needed to reassign None, 
                                        # and make sure it wont popup once you start playing :/
        screen.blit(menu_font.render(f'Player reached {player.score} points and won', False, ("White")), (20, height - 400))
    if score == 0: pass
    else: screen.blit(menu_font.render(f'Opponent reached {opponent.score} points and won', False, ("White")), (20, height - 400))




player = Paddle("Player", 10)
opponent = Paddle("Opponent", (width - 10))
ball = Ball()
title_font = pygame.font.Font("static/Pixeltype.ttf", 120)
menu_font = pygame.font.Font("static/bit5x3.ttf", 60)
score_font = pygame.font.Font("static/bit5x3.ttf", 80)
on_off = 0
comp = False



while True:
    screen.fill((0, 0, 0))
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
                on_off += 1

        if game_active == False:

            if event.type == pygame.KEYDOWN and event.key != pygame.K_g:
                ball.init()
                player.score, opponent.score = 0, 0
                player = Paddle("Player", 10)
                opponent = Paddle("Opponent", (width - 10))
                game_active = True

                if event.key == pygame.K_2:
                    computer = Computer("Computer", (width-10))
                    comp = True
        
        

    if game_active:
        player.rect.y += player.speed
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        if comp:
            computer.speed()
        else: opponent.rect.y += opponent.speed

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