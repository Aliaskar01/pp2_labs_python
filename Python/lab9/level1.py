import pygame, sys
from worm import Snake

pygame.init()

def level1(score):
    window = pygame.display.set_mode((850, 600))

    clock = pygame.time.Clock()
    fps = 5

    font = pygame.font.Font(None, 36)
    text = font.render("level1", True, (255, 255, 255))

    apple = (4, 18)

    walls = [(10, 10), (10, 11)]

    snake = Snake([(6, 4), (5, 4)], walls)

    fruit = 1

    direct = 0
    fail = False

    while len(snake.pos) < 6:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and direct != 1:
                    direct = 3
                elif e.key == pygame.K_DOWN and direct != 3:
                    direct = 1
                elif e.key == pygame.K_LEFT and direct != 0:
                    direct = 2
                elif e.key == pygame.K_RIGHT and direct != 2:
                    direct = 0

        apple, score, fruit = snake.eat(apple, score, fruit)

        if fruit == 1:
            color = (255, 0, 0)
        elif fruit == 2:
            color = (255, 255, 0)
        else:
            color = (0, 0, 255)

        score_text = font.render("score: " + str(score), True, (255, 255, 255))

        fail = snake.move(direct)
        while fail: 
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        window.fill((0, 0, 0))
        pygame.draw.rect(window, color, (25*apple[0], 25*apple[1], 25, 25))
        for i in walls:
            pygame.draw.rect(window, (122, 122, 122), (25*i[0], 25*i[1], 25, 25))
        snake.draw(window)
        window.blit(text, (750, 15))
        window.blit(score_text, (15, 15))
        pygame.display.flip()
        clock.tick(fps)
    
    return score