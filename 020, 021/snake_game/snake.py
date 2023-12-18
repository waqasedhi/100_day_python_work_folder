from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def move(self):
        for squ in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[squ - 1].xcor()
            new_y = self.squares[squ - 1].ycor()
            self.squares[squ].goto(new_x, new_y)
        self.squares[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.squares[0].heading() == 0 or self.squares[0].heading() == 180:
            self.squares[0].setheading(90)

    def down(self):
        if self.squares[0].heading() == 0 or self.squares[0].heading() == 180:
            self.squares[0].setheading(270)

    def left(self):
        if self.squares[0].heading() == 90 or self.squares[0].heading() == 270:
            self.squares[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.squares[0].setheading(0)


