from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.hideturtle()
        self.write(f"Score : 0", False, "center", ("Arial", 20, "normal"))

    def raise_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score}", False, "center", ("Arial", 20, "normal"))

