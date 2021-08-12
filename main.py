from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
all_turtles = []
for position in starting_positions:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white", "white")
    new_turtle.penup()
    new_turtle.setposition(position)
    all_turtles.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for turtle_index in range(len(all_turtles) - 1, 0, -1):
        all_turtles[turtle_index].setposition(all_turtles[turtle_index - 1].pos())
    all_turtles[0].forward(20)
screen.exitonclick()
