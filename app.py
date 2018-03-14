from pygame.locals import *
import pygame
import player
import maze

class App:
    window_width = 800
    window_height = 600
    player = 0
    x = 32
    y = 32

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._clock = pygame.time.Clock()
        self.player = player.Player()
        self.maze = maze.Maze(self.x, self.y)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE)
        pygame.display.set_caption("Battle tanks")
        self._running = True

    def on_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.rect(self._display_surf, (0, 128, 255), pygame.Rect(self.player.x, self.player.y, self.x, self.y))
        self.maze.load_maze("draw", self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.maze.load_maze("fill", None)

        while self._running:
            self.on_quit()
            
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                if not self.maze.check_collision(self.player.x, self.player.y, "right"):
                    self.player.move_right()

            if keys[K_LEFT]:
                if not self.maze.check_collision(self.player.x, self.player.y, "left"):
                    self.player.move_left()

            if keys[K_UP]:
                if not self.maze.check_collision(self.player.x, self.player.y, "up"):
                    self.player.move_up()

            if keys[K_DOWN]:
                if not self.maze.check_collision(self.player.x, self.player.y, "down"):
                    self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            self.on_render()
            self._clock.tick(120)
        
        self.on_cleanup()
