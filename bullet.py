import pygame as pg
vec = pg.math.Vector2

class Bullet(pg.sprite.Sprite):
    lifetime = 3000
    speed = 2

    def __init__(self, game, pos, dir):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load("img\\bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        game.all_sprites.add(self)
        self.pos = vec(pos)
        self.rect.center = pos
        self.vel = dir * self.speed
        self.spawn_time = pg.time.get_ticks()
        self.mask = pg.mask.from_surface(self.image)
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if pg.time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()
        if pg.sprite.spritecollideany(self, self.game.maze.walls, pg.sprite.collide_mask):
            self.kill()
            self.game.player.last_shot = 0