import pygame as pg
import player
import maze

class App:
    window_width = 800
    window_height = 800

    def on_init(self):
        pg.init()
        self._running = True
        self.screen = pg.display.set_mode((self.window_width, self.window_height), pg.HWSURFACE)
        pg.display.set_caption("Battle tanks")
        self.player = player.Player(self)
        self.maze = maze.Maze(None, 0, 0)
        self.maze.load_maze()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)
        for wall in self.maze.walls.sprites():
            self.all_sprites.add(wall)
        self._clock = pg.time.Clock()

    def on_quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._running = False

    def on_render(self):
        self.screen.fill((100, 100, 100))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.on_quit()
            
            pg.event.pump()
            keys = pg.key.get_pressed()
            self.player.update()
            if self.player.bullet is not None:
                self.player.bullet.update()

            if keys[pg.K_ESCAPE]:
                self._running = False

            self.on_render()
            self._clock.tick(60)
        
        self.on_cleanup()
