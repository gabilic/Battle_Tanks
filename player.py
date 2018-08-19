from pygame.locals import *
import pygame

class Player(pygame.sprite.Sprite):
    x = 32
    y = 32
    w = 29
    h = 29
    speed = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img\\tank.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player, walls):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            player.rect.x += player.speed
            if pygame.sprite.spritecollide(player, walls, False, pygame.sprite.collide_mask):
                player.rect.x -= player.speed

        if keys[K_LEFT]:
            player.rect.x -= player.speed
            if pygame.sprite.spritecollide(player, walls, False, pygame.sprite.collide_mask):
                player.rect.x += player.speed

        if keys[K_UP]:
            player.rect.y -= player.speed
            if pygame.sprite.spritecollide(player, walls, False, pygame.sprite.collide_mask):
                player.rect.y += player.speed

        if keys[K_DOWN]:
            player.rect.y += player.speed
            if pygame.sprite.spritecollide(player, walls, False, pygame.sprite.collide_mask):
                player.rect.y -= player.speed
