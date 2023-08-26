import pygame, random, math
from sys import exit




# Window initialization
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


# Paddles setup
class Paddle:
    speed = 0


    def __init__(self, name, dist):
        self.dist = dist
        self.rect =  pygame.Rect(self.dist, (height / 2) - 41, 10, 82)
        self.score = 0

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
        self.speed_x = (20 * (start_x / 10)) * start
        self.speed_y = (10 * (start_y / 10)) * start



    def limit(self):
        if ball.rect.x <= -10: 
            opponent.score += 1
            ball.init()
        if ball.rect.x >= width + 10:
            player.score += 1
            ball.init()
        if ball.rect.y <= 0: self.speed_y = self.speed_y * -1
        if ball.rect.y >= height: self.speed_y = self.speed_y * -1

        

    def collide(self):
        player_location = (((abs (((player.rect.top) - (ball.rect.y + 10)) - 9)) * math.pi) / 100)  # 0 (top) -> 50 -> 100 (bottom) ** OLD
        opponent_location = (((abs (((opponent.rect.top) - (ball.rect.y + 10)) - 9)) * math.pi) / 100)   # 0 (top) -> 1.57079 -> 3.14159 (bottom) ** NEW

        if self.rect.colliderect(player.rect):
            self.speed_y = 0
            self.speed_x = self.speed_x * -1
            self.speed_y += (round (math.cos(player_location) * 6, 4)) *-1

        if self.rect.colliderect(opponent.rect):
            self.speed_y = 0
            self.speed_x = self.speed_x * -1
            self.speed_y += (round (math.cos(opponent_location) * 6, 4)) *-1
        # print(self.speed_y)



player = Paddle("player", 10)
opponent = Paddle("opponent", (width - 10))

ball = Ball()

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



    pygame.display.update()
    pygame.time.Clock().tick(60)