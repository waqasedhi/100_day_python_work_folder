from turtle import Turtle
align = "center"
font = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'score: {self.score}', align=align, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=align, font=font)


    def count(self):
        self.score += 1
        self.clear()
        self.update_score()
