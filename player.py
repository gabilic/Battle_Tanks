class Player:
    x = 32
    y = 32
    w = 29
    h = 29
    speed = 1

    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed
