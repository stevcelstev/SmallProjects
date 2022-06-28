import turtle
import winsound

window = turtle.Screen()
window.title("Pong in Python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_l = 0
score_r = 0
max_score = 10
who_won = ''

# Paleta stanga
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_len=1, stretch_wid=5)
paddle_l.color("white")
paddle_l.penup()
paddle_l.goto(-350, 0)

# Paleta dreapta
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_len=1, stretch_wid=5)
paddle_r.color("white")
paddle_r.penup()
paddle_r.goto(350, 0)

# Minge
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen (scorul)
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functii

def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)


def reset_game():
    paddle_l.goto(-350, 0)
    paddle_r.goto(350, 0)
    ball.goto(0, 0)
    if who_won == 1:
        ball.dx = -0.2
    elif who_won == 2:
        ball.dx = 0.2
    ball.dy = 0.2
    score.clear()
    score.write("Player 1: {}  Player 2: {}".format(score_l, score_r), align="center",
                font=("Courier", 24, "normal"))


def close_game():
    window.bye()


# Keyboard binding

window.listen()
window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "Up")
window.onkeypress(paddle_r_down, "Down")
window.onkeypress(reset_game, "r")
window.onkeypress(close_game, "q")

# Aici este main game loop-ul
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_l, score_r), align="center",
                    font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_l, score_r), align="center",
                    font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_r.ycor() + 40 > ball.ycor() > paddle_r.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_l.ycor() + 40 > ball.ycor() > paddle_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score_l == max_score:
        score_l = 0
        score_r = 0
        score.clear()
        score.write("Player 1 has won", align="center", font=("Courier", 24, "normal"))
        paddle_l.goto(-350, 0)
        paddle_r.goto(350, 0)
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        who_won = 1

    if score_r == max_score:
        score_l = 0
        score_r = 0
        score.clear()
        score.write("Player 2 has won", align="center", font=("Courier", 24, "normal"))
        paddle_l.goto(-350, 0)
        paddle_r.goto(350, 0)
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        who_won = 1
