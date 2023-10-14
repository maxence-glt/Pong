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
title_font = pygame.font.Font("static/Pixeltype.ttf", 120)
menu_font = pygame.font.Font("static/bit5x3.ttf", 60)
score_font = pygame.font.Font("static/bit5x3.ttf", 80)


# Paddles setup class
class Paddle:
    speed = 0

    # initializes a paddle
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

    # defines the limits of the screen the paddles can move to
    def limits(self):
        if self.rect.top <= 0: self.rect.top = 0
        elif self.rect.bottom >= height: self.rect.bottom = height
    
    # the player input section
    def input(self):
        if event.type == pygame.KEYDOWN:
            if event.key == self.up_K: self.speed -= 11
            if event.key == self.down_K: self.speed += 11

        if event.type == pygame.KEYUP:
            if event.key == self.up_K: self.speed += 11
            if event.key == self.down_K: self.speed -= 11
    

# The Pong ball class
class Ball:
    speed = 13
    
    # initializes the ball, setting it to the exact middle of the screen
    def __init__(self):
        self.rect = pygame.Rect(width/2 - 10, height/2 - 10, 20, 20)

    # this resets the ball to the middle of the screen after moving around
    def init(self):
        self.rect.x, self.rect.y = width / 2 - 10, height / 2 - 10
        
        # this randomizes the direction and speed of the ball when initialized
        start, start_x, start_y = random.randint(-1, 0), random.randint(7, 9), random.randint(1, 4)
        if start == 0: start += 1

        self.speed_x = Ball.speed * start
        self.speed_y = (5 * (start_y / 10)) * start
        self.speed_x_original = (25 * (start_x / 10)) * start

    # the limits the ball can go to, and the behavior it exhibts when coliding with said limits
    def limit(self):
        if ball.rect.x <= -15: 
            opponent.score += 1
            ball.init()
        if ball.rect.x >= width + 15:
            player.score += 1
            ball.init()
        if ball.rect.y <= 0 or ball.rect.y >= height: self.speed_y = self.speed_y * -1

    # the equation for the angle of incidence once the ball collides with a paddle
    # I first get the balls location by subtracting the paddle and ball's y locations
    # I convert the location to a 1-100 scale and multiply by pi, divide by 100 and take the cosine
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


# Computer class
class Computer(Paddle):
    
    # Simple AI that tracks ball at an interval, as well as moves paddle back to middle once ball goes past 2/3 mark
    def speed(self):
        if ball.rect.x > width * (1/3):
            if ball.rect.y < opponent.rect.y + 30:
                opponent.rect.y += -8

            if ball.rect.y > opponent.rect.y + 50:
                opponent.rect.y += 8

            else:
                opponent.rect.y += 0
        else:
            if height / 2 > opponent.rect.y + 30:
                opponent.rect.y += 8
            if height / 2 < opponent.rect.y + 50:
                opponent.rect.y += -8
            else:
                opponent.rect.y += 0


# main menu function that shows the winners points score (if no one played yet, it doesn't show the scores)
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


# creating the classes
player = Paddle("Player", 10)
opponent = Paddle("Opponent", (width - 10))
ball = Ball()

# sets everything to off so the player can choose what they want in menu
game_active = False
on_off = 0
comp = False


while True:
    screen.fill((0, 0, 0))
    
    # event loop
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

        # keeps checking that the player and the ball don't go out of bounds
        player.limits()
        opponent.limits()
        ball.limit()
        ball.collide()

        # draws everything on screen
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
            menu(player.score, player.name)
        if opponent.score > player.score: 
            menu(opponent.score, opponent.name)
        else: menu(0, None)


    pygame.display.update()
    pygame.time.Clock().tick(60)
