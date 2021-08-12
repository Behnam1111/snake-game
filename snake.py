from turtle import Turtle


class Snake:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.all_turtles = []
        self.create_snake()

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
        self.all_turtles[0].forward(20)

    def up(self):
        self.all_turtles[0].setheading(90)
        self.move()

    def left(self):
        self.all_turtles[0].setheading(180)
        self.move()

    def down(self):
        self.all_turtles[0].setheading(270)
        self.move()

    def right(self):
        self.all_turtles[0].setheading(0)
        self.move()


