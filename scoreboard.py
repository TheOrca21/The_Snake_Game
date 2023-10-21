from turtle import Turtle
ALIGN = "center"
FONT = ("Comic Sans MS", 21, "normal")


class Score(Turtle):

    score: int

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt", 'r') as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} High Score:{self.high_score}", False, ALIGN, FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('Data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def collision(self):
        self.score += 1
        self.update_score()

