from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.hideturtle()
        self.show_score()

    def raise_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.write_high_score_to_file()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, "center", ("Arial", 20, "normal"))

    def read_high_score_from_file(self):
        with open("highscore.txt") as file_handler:
            highscore = int(file_handler.read())
            return int(highscore)

    def write_high_score_to_file(self):
        with open("highscore.txt", "w") as file_handler:
            file_handler.write(f"{self.high_score}")
