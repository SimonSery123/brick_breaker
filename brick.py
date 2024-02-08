import pygame


class Brick:
    def __init__(self, game, x, y, health):
        self.x = x
        self.y = y
        self.settings = game.settings
        self.width = self.settings.brick_width
        self.height = self.settings.brick_height
        self.health = health
        self.max_health = health
        self.color = self.settings.brick_color[0]

        self.window = game.window
        self.ball = game.ball

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

    def interpolate(self, color_a, color_b, t):
        return tuple(int((a + (b - a) * t)) for a, b in zip(color_a, color_b))

    def collide(self):
        if not (self.x + self.width >= self.ball.x >= self.x):
            return False

        if not (self.ball.y - self.ball.radius <= self.y + self.height):
            return False

        self.hit()
        self.ball.set_vel(self.ball.x_vel, self.ball.y_vel * -1)

        return True

    def hit(self):
        self.health -= 1
        self.color = self.interpolate(*self.settings.brick_color, self.health / self.max_health)
