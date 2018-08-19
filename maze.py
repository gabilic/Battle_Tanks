from random import shuffle, randrange
import pygame

class Maze(pygame.sprite.Sprite):
    x = 32
    y = 32
    w = 31
    h = 31
    thin_w = 11
    thin_h = 11
    
    def __init__(self, wall, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_dict = {"wall": pygame.image.load("img\\wall.png").convert_alpha(),
                           "wall_e": pygame.image.load("img\\wall_e.png").convert_alpha(),
                           "wall_ens": pygame.image.load("img\\wall_ens.png").convert_alpha(),
                           "wall_ensw": pygame.image.load("img\\wall_ensw.png").convert_alpha(),
                           "wall_es": pygame.image.load("img\\wall_es.png").convert_alpha(),
                           "wall_ew": pygame.image.load("img\\wall_ew.png").convert_alpha()}
        self.walls = pygame.sprite.Group()
        self.M = 25
        self.N = 25
        self.block_list = []
        self.maze = []
        self.generate_maze()
        if wall is not None:
            self.image = wall
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.mask = pygame.mask.from_surface(self.image)

    def generate_maze(self):
        w = (self.M - 1) // 2
        h = (self.N - 1) // 2
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["10"] * w + ['1'] for _ in range(h)] + [[]]
        hor = [["11"] * w + ['1'] for _ in range(h + 1)]
     
        def walk(x, y):
            vis[y][x] = 1
     
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "10"
                if yy == y: ver[y][max(x, xx)] = "00"
                walk(xx, yy)
     
        walk(randrange(w), randrange(h))
     
        maze = ""
        for (a, b) in zip(hor, ver):
            maze += ''.join(a + ['\n'] + b + ['\n'])
        self.maze = [int(i) for i in maze if i != "\n"]

    def load_maze(self):
        for i in range(self.M * self.N):
            x = (i % self.M) * self.x
            y = (i // self.M) * self.y
            if self.maze[i] == 1:
                if i // self.M == 0 or i // self.M == self.N - 1 or i % self.M == 0 or i % self.M == self.M - 1:
                    wall = Maze(self.image_dict["wall"], x, y)
                    self.walls.add(wall)
                else:
                    if self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        wall = Maze(self.image_dict["wall_e"], x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_e"], 270), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_e"], 180), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_e"], 90), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        wall = Maze(self.image_dict["wall_ens"], x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_ens"], 270), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_ens"], 180), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_ens"], 90), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        wall = Maze(self.image_dict["wall_es"], x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_es"], 270), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_es"], 180), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_es"], 90), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        wall = Maze(self.image_dict["wall_ew"], x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        wall = Maze(pygame.transform.rotate(self.image_dict["wall_ew"], 90), x, y)
                        self.walls.add(wall)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        wall = Maze(self.image_dict["wall_ensw"], x, y)
                        self.walls.add(wall)
