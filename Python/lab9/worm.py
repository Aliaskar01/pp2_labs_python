import pygame
import random

class Snake:
    def __init__(self, pos, walls):
        self.pos = pos
        self.possible_possition = [(i, j) for i in range(34) for j in range(24)]
        self.possible_possition.append((-1, -1))
        self.time = 0
        
        for i in pos:
            self.possible_possition.remove(i)
        for i in walls:
            self.possible_possition.remove(i)

    def move(self, direct):
        if direct == 0:
            self.pos.insert(0, (self.pos[0][0]+1, self.pos[0][1]))
        elif direct == 1:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]+1))
        elif direct == 2:
            self.pos.insert(0, (self.pos[0][0]-1, self.pos[0][1]))
        else:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]-1))
        try:
            self.possible_possition.remove(self.pos[0])
        except:
            return True
        self.possible_possition.append(self.pos[-1])
        self.pos.pop()

    def eat(self, a, s, t):
        self.time += 1
        if self.pos[0][0] == a[0] and self.pos[0][1] == a[1] or self.time > 30:
            self.possible_possition.remove((-1, -1))
            a = random.choice(self.possible_possition)
            if self.time > 30:
                self.possible_possition.append((-1, -1))
            else:
                self.pos.append((-1, -1))
                s += t
            self.time = 0 
            t = random.randint(1, 3)
        return a, s, t

    def draw(self, window):
        for i in range(len(self.pos)):
            pygame.draw.rect(window, (0, 255, 0), (self.pos[i][0]*25, self.pos[i][1]*25, 25, 25))
