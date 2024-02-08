class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (137, 207, 240)

        self.fps = 60
        self.ball_radius = 10
        self.ball_speed = 7
        self.ball_color = (252, 3, 3)

        self.cols = 10
        self.rows = 3

        self.brick_width = self.screen_width // self.cols - 2
        self.brick_height = 20

        self.paddle_width = 120
        self.paddle_height = 15
        self.paddle_speed = 5
        self.paddle_color = (143, 81, 74)
        self.lives = 3
        self.brick_color = [(60, 60, 60), (199, 117, 117)]
