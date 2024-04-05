import pygame
import sys
import random
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((840, 600))

pygame.display.set_caption("Game")

road =  pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab8\img\road.png')

FPS = 60
FramePerSec = pygame.time.Clock()

speed = 3

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Verdana", 100)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

coin = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab8\img\coin.png')
coin.set_colorkey(WHITE)
coin = pygame.transform.scale(coin, (20, 20))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab8\img\car1.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (102, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, score):
        fail = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.x > 140:
            self.rect.x -= 3 * speed
        if keys[pygame.K_d] and self.rect.x < 605:
            self.rect.x += 3 * speed

        if pygame.sprite.spritecollide(self, cars, False):
            fail = True
        if pygame.sprite.spritecollide(self, coins, False):
            coin_in_road.rect.y = - 200
            lines = [190, 320, 440, 570]
            line = random.randint(0, 3)
            coin_in_road.rect.x = lines[line]
            score += 1
        
        return fail, score
    
    def draw(self):
        window.blit(self.image, self.rect)

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab8\img\car2.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        lines = [180, 300, 440, 570]
        self.rect.y += 2 * speed
        line = random.randint(0, 3)
        if self.rect.y > 800:
            self.rect.y = - 300
            self.rect.x = lines[line]
    
    def draw(self):
        window.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab8\img\coin.png')
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        lines = [190, 320, 440, 570]
        self.rect.y += 2 * speed
        line = random.randint(0, 3)
        if self.rect.y > 700:
            self.rect.y = - 200
            self.rect.x = lines[line]
        if pygame.sprite.spritecollide(self, cars, False):
           self.rect.y = - 200
           self.rect.x = lines[line]
    
    def draw(self):
        window.blit(self.image, self.rect)

player = Player(180, 430)

cars = pygame.sprite.Group()
coins = pygame.sprite.Group()

coin_in_road = Coin(190, -100)
coins.add(coin_in_road)

for i in range(2):
    car = Car(570, 130)
    cars.add(car)
    car = Car(570, -330)
    cars.add(car)

y1 = 0
y2 = -650

fail = False

score = 0

while not fail:
    window.fill((0, 0, 0))
    window.blit(road, (0, y1))
    window.blit(road, (0, y2))

    score_txt = font_small.render(str(score), True, YELLOW)
    window.blit(score_txt, (50, 50))
    window.blit(coin, (20, 52))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y1 += speed
    y2 += speed
    if y1 >= 650:
        y1 = -650
    elif y2 >= 650:
        y2 = -650

    for i in cars:
        i.update()
        i.draw()

    coin_in_road.update()
    coin_in_road.draw()
    
    fail, score = player.update(score)
    player.draw()
    

    pygame.display.update()
    FramePerSec.tick(FPS)

while fail:
    window.fill(RED)
    window.blit(game_over, (150, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()