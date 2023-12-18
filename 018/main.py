import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# print(tim)
# tim.shape("turtle")
# tim.color("red", "green")  #change the color

# video 003
# for i in range(4):   # make a square
#     tim.lt(90)
#     tim.fd(100)

# video 005
# for _ in range(10):  # make a dash line
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()

# video 006
# a = 360    # make a loop to make triangle, square, other
# b = 3
# c = 100
# e = 8
# colors = ["red", "light blue", "black", "yellow", "purple", "cyan", "green", "orange"]
# for _ in range(e):
#     tim.color(random.choice(colors))
#     d = a / b
#     for _ in range(b):
#         tim.fd(c)
#         tim.rt(d)
#     b += 1

# video 007 008

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

# colors = ["red", "light blue", "black", "yellow", "purple", "cyan", "green", "orange"]

#
# tim.width(10)
# direct = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random_color())  # (random.choice(colors))
#     tim.setheading(random.choice(direct))
#     tim.fd(25)


# tim.circle(50)

# t.home()
# t.position()
# t.heading()
# t.circle(50)
# t.position()
# t.heading()
# t.circle(120, 360)  # draw a semicircle
# t.position()
# t.heading()

# video 009
# def draw_spirograph(gap_size):
#     for _ in range(int(360/gap_size)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap_size)
#
#
# draw_spirograph(5)
video



screen = t.Screen()
print(screen)
screen.exitonclick()
