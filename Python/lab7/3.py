import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500, 500))

x = 225
y = 225

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20
                if y < 25:
                    y = 25
            elif event.key == pygame.K_DOWN:
                y += 20
                if y > 475:
                    y = 475
            elif event.key == pygame.K_LEFT:
                x -= 20
                if x < 25:
                    x = 25
            elif event.key == pygame.K_RIGHT:
                x += 20
                if x > 475:
                    x = 475
    
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (255, 0, 0), (x, y), 25)
    pygame.display.update()