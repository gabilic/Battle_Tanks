from random import shuffle, randrange
import pygame

class Maze(pygame.sprite.Sprite):
    w = 31
    h = 31
    thin_w = 11
    thin_h = 11
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.M = 25
        self.N = 25
        self.x = x
        self.y = y
        self.block_list = []
        self.maze = []
        self.image_surf = {"wall": pygame.image.load("img\\wall.png"),
                           "wall_e": pygame.image.load("img\\wall_e.png"),
                           "wall_ens": pygame.image.load("img\\wall_ens.png"),
                           "wall_ensw": pygame.image.load("img\\wall_ensw.png"),
                           "wall_es": pygame.image.load("img\\wall_es.png"),
                           "wall_ew": pygame.image.load("img\\wall_ew.png")}

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

    def load_maze(self, option, display_surf):
        for i in range(self.M * self.N):
            x = (i % self.M) * self.x
            y = (i // self.M) * self.y
            if self.maze[i] == 1:
                if i // self.M == 0 or i // self.M == self.N - 1 or i % self.M == 0 or i % self.M == self.M - 1:
                    if option == "draw": display_surf.blit(self.image_surf["wall"], (x, y))
                    elif option == "fill": self.block_list.append({'x': x, 'y': y, 'w': self.w, 'h': self.h})
                else:
                    if self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(self.image_surf["wall_e"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_e"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_e"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_e"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(self.image_surf["wall_ens"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_ens"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_ens"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_ens"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(self.image_surf["wall_es"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                            self.fill_maze(x, y, "s", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_es"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                            self.fill_maze(x, y, "w", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_es"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                            self.fill_maze(x, y, "n", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_es"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                            self.fill_maze(x, y, "e", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(self.image_surf["wall_ew"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(self.image_surf["wall_ew"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(self.image_surf["wall_ensw"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", True)
                            self.fill_maze(x, y, "s", True)

    def fill_maze(self, x, y, side, wide_wall):
        if wide_wall:
            if side == "e":
                self.block_list.append({'x': x, 'y': y + self.thin_h, 'w': self.w, 'h': self.h - self.thin_h * 2})
            elif side == "s":
                self.block_list.append({'x': x + self.thin_w, 'y': y, 'w': self.w - self.thin_w * 2, 'h': self.h})
        else:
            if side == "e":
                self.block_list.append({'x': x + self.thin_w, 'y': y + self.thin_h, 'w': self.w - self.thin_w, 'h': self.h - self.thin_h * 2})
            elif side == "s":
                self.block_list.append({'x': x + self.thin_w, 'y': y + self.thin_h, 'w': self.w - self.thin_w * 2, 'h': self.h - self.thin_h})
            elif side == "w":
                self.block_list.append({'x': x, 'y': y + self.thin_h, 'w': self.w - self.thin_w, 'h': self.h - self.thin_h * 2})
            elif side == "n":
                self.block_list.append({'x': x + self.thin_w, 'y': y, 'w': self.w - self.thin_w * 2, 'h': self.h - self.thin_h})
                
    def check_collision(self, player, side):
        collision = False

        for block in self.block_list:
            
            if side == "right":
                if block['x'] <= player.rect.x + player.w + 1 < block['x'] + block['w'] and block['y'] <= player.rect.y + player.h and player.rect.y <= block['y'] + block['h']:
                    collision = True

            if side == "left":
                if block['x'] < player.rect.x - 1 <= block['x'] + block['w'] and block['y'] <= player.rect.y + player.h and player.rect.y <= block['y'] + block['h']:
                    collision = True

            if side == "up":
                if block['x'] <= player.rect.x + player.w and player.rect.x <= block['x'] + block['w'] and block['y'] < player.rect.y - 1 <= block['y'] + block['h']:
                    collision = True

            if side == "down":
                if block['x'] <= player.rect.x + player.w and player.rect.x <= block['x'] + block['w'] and block['y'] <= player.rect.y + player.h + 1 < block['y'] + block['h']:
                    collision = True

        return collision
