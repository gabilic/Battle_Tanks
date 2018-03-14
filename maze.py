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
        self.block_list = []
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def load_maze(self, option, display_surf):
        for i in range(self.M * self.N):
            x = (i % self.M) * self.x
            y = (i // self.M) * self.y
            if self.maze[i] == 1:
                if option == "draw": pygame.draw.rect(display_surf, (255, 100, 0), pygame.Rect(x, y, self.x, self.y))
                elif option == "fill": self.block_list.append({'x': x, 'y': y, 'w': self.w, 'h': self.h})

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
