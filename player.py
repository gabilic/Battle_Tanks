import pygame

class Player(pygame.sprite.Sprite):
    x = 32
    y = 32
    w = 29
    h = 29
    speed = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img\\tank.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
