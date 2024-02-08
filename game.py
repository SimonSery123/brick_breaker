import pygame

from paddle import Paddle
from settings import Settings
from ball import Ball
import math
from brick import Brick


class BrickBreaker:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Brick breaker")

        pygame.font.SysFont("ubuntu", 40)

        self.paddle = Paddle(self, self.settings.paddle_width, self.settings.paddle_height, self.settings.paddle_color)

        self.paddle.reset_position()

        self.ball = Ball(self, self.paddle.x + self.paddle.width // 2, self.paddle.y - self.settings.ball_radius,
                         self.settings.ball_color)

        self.bricks = self.generate_bricks(self.settings.rows, self.settings.cols)

    def draw(self):
        self.window.fill(self.settings.bg_color)

        for brick in self.bricks:
            brick.draw()

        self.ball.draw()
        self.paddle.draw()
        pygame.display.update()

    def generate_bricks(self, rows, cols):
        gap = 2
        bricks = []
        for row in range(rows):
            for col in range(cols):
                gap_row = gap * row
                gap_col = gap * col
                # extra_space = 2 * gap

                brick = Brick(self, col * self.settings.brick_width + gap_col,
                              row * self.settings.brick_height + gap_row, 2)
                bricks.append(brick)

        return bricks

    def ball_paddle_collision(self):
        if not (
            self.ball.x + self.ball.radius >= self.paddle.x and
            self.ball.x - self.ball.radius <= self.paddle.x + self.paddle.width and
            self.ball.y + self.ball.radius >= self.paddle.y
        ):
            return

        paddle_center = self.paddle.x + self.paddle.width // 2
        distance_to_center = self.ball.x - paddle_center

        percent_width = distance_to_center / self.paddle.width
        angle = percent_width * 90
        angle_radians = math.radians(angle)

        x_vel = math.sin(angle_radians) * self.settings.ball_speed
        y_vel = math.cos(angle_radians) * self.settings.ball_speed * -1

        self.ball.set_vel(x_vel, y_vel)

    def run(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            clock.tick(self.settings.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.paddle.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.paddle.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.paddle.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.paddle.moving_left = False

            if self.ball.y + self.ball.radius >= self.settings.screen_height:
                self.ball.set_vel(0, self.settings.ball_speed * -1)
                return

            self.ball_paddle_collision()
            self.ball.collision()

            for brick in self.bricks[:]:
                brick.collide()

                if brick.health <= 0:
                    self.bricks.remove(brick)


            self.ball.move()
            self.paddle.move()
            self.draw()

        pygame.quit()
        quit()

if __name__ == "__main__":
    brick_breaker = BrickBreaker()
    brick_breaker.run()

