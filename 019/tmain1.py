from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# video 002
# def move_forward():
#     tim.fd(10)
#
#
# screen.listen()
# screen.onkey(move_forward, "space")


def forward():
    tim.fd(10)


def backward():
    tim.bk(10)


def right():
    tim.rt(10)


def left():
    tim.lt(10)


def reset_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(reset_screen, "c")







screen.exitonclick()
