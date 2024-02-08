import pygame

class Paddle:
    def __init__(self, game, width, height, color):
        self.settings = game.settings
        self.window = game.window

        self.width = width
        self.height = height
        self.color = color

        self.moving_left = False
        self.moving_right = False

        self.x = 0
        self.y = 0

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.moving_left and self.x - self.settings.paddle_speed >= 0:
            self.x -= self.settings.paddle_speed

        if self.moving_right and self.x + self.width + self.settings.paddle_speed <= self.settings.screen_width:
            self.x += self.settings.paddle_speed

    def reset_position(self):
        self.x = self.window.get_width() / 2 - self.width // 2
        self.y = self.window.get_height() - self.height - 5
