from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        self.goto(x, y)
