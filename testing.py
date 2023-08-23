import pygame, random
from sys import exit




# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


# Paddles setup
class Paddle:
    speed = 0
    score = 0


    def __init__(self, name, dist):
        self.dist = dist
        self.rect =  pygame.Rect(self.dist, (height / 2) - 70, 10, 140)

        if name == "player": 
            self.up_K = pygame.K_w
            self.down_K = pygame.K_s
        elif name == "opponent":
            self.up_K = pygame.K_UP
            self.down_K = pygame.K_DOWN    


    def limits(self):
        if self.rect.top <= 0: self.rect.top = 0
        elif self.rect.bottom >= height: self.rect.bottom = height
    

    def input(self):
        if event.type == pygame.KEYDOWN:
            if event.key == self.up_K: self.speed -= 7
            if event.key == self.down_K: self.speed += 7
        if event.type == pygame.KEYUP:
            if event.key == self.up_K: self.speed += 7
            if event.key == self.down_K: self.speed -= 7
    




class Ball:
    player_score = 0
    opponent_score = 0
    
    def __init__(self):
        self.rect = pygame.Rect(width/2, height /2, 20, 20)
        self.speed_x = 0
        self.speed_y = 0

    def init(self):
        self.rect.x, self.rect.y = width / 2 - 10, height / 2 - 10
        self.speed_x, self.speed_y = 0, 0
        start = random.randint(0, 1)
        if start == 0: self.speed_x -= 10
        if start == 1: self.speed_x += 10

    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def ball_limit(self):
        if ball.rect.x <= -10: 
            self.opponent_score += 1
            ball.init()
        if ball.rect.x >= width + 10:
            self.player_score += 1
            ball.init()
        if ball.rect.y == 0: self.speed_y = self.speed_y * -1
        if ball.rect.y == height: self.speed_y = self.speed_y * -1

    def collide(self):
        player_location = (player.rect.y + 70) - (ball.rect.y + 10)     # 0 -> 660
        opponent_location = (player.rect.y + 70) - (ball.rect.y + 10)

        if self.rect.colliderect(player.rect):
            if player_location in range(-15, 16): self.speed_y = 0
            elif player_location < -15: 
                self.speed_y = 0
                self.speed_y += 10
            elif player_location > 16: 
                self.speed_y = 0
                self.speed_y -= 10
            self.speed_x = self.speed_x * -1

        if self.rect.colliderect(opponent.rect): 
            if opponent_location in range(-15, 16): self.speed_y = 0
            elif opponent_location < -15: 
                ball_speed_y = 0
                ball_speed_y += 10
            elif opponent_location > 16: 
                ball_speed_y = 0
                ball_speed_y -= 10
            self.speed_x = self.speed_x * -1

        ball.rect.x += self.speed_x
        ball.rect.y += self.speed_y





player = Paddle("player", 10)

opponent = Paddle("opponent", (width - 10))

ball = Ball()





# Score
score_font = pygame.font.Font("bit5x3.ttf", 80)





# Game loop
ball.init()





while True:
    screen.fill((0, 0, 0))





    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player.input()
        opponent.input()






    player.rect.y += player.speed
    opponent.rect.y += opponent.speed
    ball.rect.x += ball.speed_x


    # Control
    player.limits()
    opponent.limits()
    ball.ball_limit()
    ball.collide()

    # Draw
    pygame.draw.rect(screen, "White", player.rect)
    pygame.draw.rect(screen, "White", opponent.rect)
    pygame.draw.ellipse(screen, "White", ball.rect)
    pygame.draw.aaline(screen, "White", (width / 2, 0),(width / 2, height))

    screen.blit(score_font.render(f"{ball.player_score}", False, "White"), ((width / 2) - 120, 50))
    screen.blit(score_font.render(f"{ball.opponent_score}", False, "White"), ((width / 2) + 100, 50))




    pygame.display.update()
    pygame.time.Clock().tick(60)