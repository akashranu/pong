from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dir = 10
        self.y_dir = 10
        self.movement_s = 0.1

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_dir *= -1 #because the ball will change y way with a reflection after bounce

    def paddle_contact(self):
        self.x_dir *= -1
        self.movement_s *= 0.9

    def refresh_ball(self):
        self.goto(0,0)
        self.movement_s = 0.1

    def opp_chance(self):
        self.x_dir *= -1
