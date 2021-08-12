from turtle import Turtle


class Snake:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in self.starting_positions:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white", "white")
            new_turtle.penup()
            new_turtle.setposition(position)
            self.all_turtles.append(new_turtle)

    def move(self):
        for turtle_index in range(len(self.all_turtles) - 1, 0, -1):
            self.all_turtles[turtle_index].setposition(self.all_turtles[turtle_index - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 180:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


