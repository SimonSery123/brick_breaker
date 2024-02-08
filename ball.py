import pygame

class Ball:
    def __init__(self, game, x, y, color):
        self.game = game
        self.settings = game.settings

        self.x = x
        self.y = y
        self.radius = self.settings.ball_radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.settings.ball_speed

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self):
        pygame.draw.circle(self.game.window, self.color, (self.x, self.y), self.radius)

    def collision(self):
        if self.x - self.settings.ball_radius <= 0 or self.x + self.settings.ball_radius >= self.settings.screen_width:
            self.set_vel(self.x_vel * -1, self.y_vel)

        if self.y + self.settings.ball_radius >= self.settings.screen_height or self.y - self.settings.ball_radius <= 0:
            self.set_vel(self.x_vel, self.y_vel * -1)

