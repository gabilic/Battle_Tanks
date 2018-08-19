from pygame.locals import *
import pygame
import player
import maze

class App:
    window_width = 800
    window_height = 800

    def on_init(self):
        pygame.init()
        self._running = True
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE)
        pygame.display.set_caption("Battle tanks")
        self.player = player.Player()
        self.maze = maze.Maze()
        self._clock = pygame.time.Clock()

    def on_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False

    def on_render(self):
        self.screen.fill((100, 100, 100))
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.maze.load_maze("draw", self.screen)
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
                if not self.maze.check_collision(self.player, "right"):
                    self.player.move_right()

            if keys[K_LEFT]:
                if not self.maze.check_collision(self.player, "left"):
                    self.player.move_left()

            if keys[K_UP]:
                if not self.maze.check_collision(self.player, "up"):
                    self.player.move_up()

            if keys[K_DOWN]:
                if not self.maze.check_collision(self.player, "down"):
                    self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            self.on_render()
            self._clock.tick(120)
        
        self.on_cleanup()
