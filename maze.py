import pygame

class Maze:
    x = 0
    y = 0
    w = 32
    h = 32
    thin_w = 11
    thin_h = 11
    
    def __init__(self, x, y):
        self.M = 11
        self.N = 11
        self.x = x
        self.y = y
        self.block_list = []
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
                     1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def load_maze(self, option, display_surf, image_surf):
        for i in range(self.M * self.N):
            x = (i % self.M) * self.x
            y = (i // self.M) * self.y
            if self.maze[i] == 1:
                if i // self.M == 0 or i // self.M == self.N - 1 or i % self.M == 0 or i % self.M == self.M - 1:
                    if option == "draw": display_surf.blit(image_surf["wall"], (x, y))
                    elif option == "fill": self.block_list.append({'x': x, 'y': y, 'w': self.w, 'h': self.h})
                else:
                    if self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(image_surf["wall_e"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_e"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_e"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_e"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(image_surf["wall_ens"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_ens"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_ens"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_ens"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(image_surf["wall_es"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", False)
                            self.fill_maze(x, y, "s", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_es"], 270), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", False)
                            self.fill_maze(x, y, "w", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_es"], 180), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "w", False)
                            self.fill_maze(x, y, "n", False)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_es"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "n", False)
                            self.fill_maze(x, y, "e", False)
                    elif self.maze[i - self.M] == 0 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 0 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(image_surf["wall_ew"], (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "e", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 0 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 0:
                        if option == "draw": display_surf.blit(pygame.transform.rotate(image_surf["wall_ew"], 90), (x, y))
                        elif option == "fill":
                            self.fill_maze(x, y, "s", True)
                    elif self.maze[i - self.M] == 1 and self.maze[i + 1] == 1 and self.maze[i + self.M] == 1 and self.maze[i - 1] == 1:
                        if option == "draw": display_surf.blit(image_surf["wall_ensw"], (x, y))
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
                
    def check_collision(self, player_x, player_y, side):
        collision = False

        for block in self.block_list:
            
            if side == "right":
                if block['x'] <= player_x + self.w <= block['x'] + block['w'] and block['y'] < player_y + self.h and player_y < block['y'] + block['h']:
                    collision = True

            if side == "left":
                if block['x'] <= player_x <= block['x'] + block['w'] and block['y'] < player_y + self.h and player_y < block['y'] + block['h']:
                    collision = True

            if side == "up":
                if block['x'] < player_x + self.w and player_x < block['x'] + block['w'] and block['y'] <= player_y <= block['y'] + block['h']:
                    collision = True

            if side == "down":
                if block['x'] < player_x + self.w and player_x < block['x'] + block['w'] and block['y'] <= player_y + self.h <= block['y'] + block['h']:
                    collision = True

        return collision
