from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
all_turtles = []
for position in starting_positions:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white", "white")
    new_turtle.setposition(position)















screen.exitonclick()
