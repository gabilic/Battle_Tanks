import pygame as pg
import bullet
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    x = 32
    y = 32
    w = 29
    h = 29
    bullet_rate = 3010
    bullet_offset = vec(18, 0)
    speed = 2
    rot_speed = 2

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.original_image = pg.image.load("img\\tank.png").convert_alpha()
        self.image = self.original_image
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vel = vec(0, 0)
        self.pos = self.rect.center
        self.rot = 0
        self.bullet = None
        self.last_shot = 0
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rot = (self.rot - self.rot_speed) % 360
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.mask = pg.mask.from_surface(self.image)
            if pg.sprite.spritecollide(self, self.game.maze.walls, False, pg.sprite.collide_mask):
                self.rot = (self.rot + self.rot_speed) % 360
                self.image = pg.transform.rotate(self.original_image, self.rot)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
                self.mask = pg.mask.from_surface(self.image)

        if keys[pg.K_LEFT]:
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.mask = pg.mask.from_surface(self.image)
            if pg.sprite.spritecollide(self, self.game.maze.walls, False, pg.sprite.collide_mask):
                self.rot = (self.rot - self.rot_speed) % 360
                self.image = pg.transform.rotate(self.original_image, self.rot)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
                self.mask = pg.mask.from_surface(self.image)

        if keys[pg.K_UP]:
            self.pos += vec(self.speed, 0).rotate(-self.rot)
            self.rect.center = self.pos
            if pg.sprite.spritecollide(self, self.game.maze.walls, False, pg.sprite.collide_mask):
                self.pos += vec(-self.speed, 0).rotate(-self.rot)
                self.rect.center = self.pos

        if keys[pg.K_DOWN]:
            self.pos += vec(-self.speed / 2, 0).rotate(-self.rot)
            self.rect.center = self.pos
            if pg.sprite.spritecollide(self, self.game.maze.walls, False, pg.sprite.collide_mask):
                self.pos += vec(self.speed / 2, 0).rotate(-self.rot)
                self.rect.center = self.pos
        
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > self.bullet_rate:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + self.bullet_offset.rotate(-self.rot)
                self.bullet = bullet.Bullet(self.game, pos, dir)
