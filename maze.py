import pygame

class Maze:
    x = 0
    y = 0
    w = 32
    h = 32
    
    def __init__(self, x, y):
        self.M = 10
        self.N = 8
        self.x = x
        self.y = y
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def load_maze(self, display_surf):
        for i in range(self.M * self.N):
            x = (i % self.M) * self.x
            y = (i // self.M) * self.y
            if self.maze[i] == 1:
                pygame.draw.rect(display_surf, (255, 100, 0), pygame.Rect(x, y, self.x, self.y))
