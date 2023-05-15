from turtle import Turtle, Screen
from Ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
paddle = Turtle()
ball = Ball()
score = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        ball.speed("fastest")

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        ball.speed("slowest")




screen.exitonclick()
