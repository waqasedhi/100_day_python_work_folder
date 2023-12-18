from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count()

    # detect collision of wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for square in snake.squares[2:] :
        if snake.head.distance(square) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
