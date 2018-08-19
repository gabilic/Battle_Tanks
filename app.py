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
        self.maze = maze.Maze(None, 0, 0)
        self.maze.load_maze()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        for wall in self.maze.walls.sprites():
            self.all_sprites.add(wall)
        self._clock = pygame.time.Clock()

    def on_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False

    def on_render(self):
        self.screen.fill((100, 100, 100))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.on_quit()
            
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            self.player.update(self.player, self.maze.walls)

            if keys[K_ESCAPE]:
                self._running = False

            self.on_render()
            self._clock.tick(120)
        
        self.on_cleanup()
