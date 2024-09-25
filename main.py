import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)


right_paddle = Paddle(350)# now we can create as many of these paddles
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

playing_game = True
ball.move()
while playing_game:
    screen.update()
    time.sleep(ball.movement_s)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_contact()

    if ball.xcor() > 380:
        scoreboard.right_point()
        ball.refresh_ball()

    if ball.xcor() < -380:
        scoreboard.left_points()
        ball.refresh_ball()





screen.exitonclick()

