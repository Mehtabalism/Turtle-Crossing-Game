from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.color("black")
        self.level_number = 1
        self.write(f"Level: {self.level_number}", align="left", font=FONT)

    def increase_level(self):
        self.level_number += 1
        self.clear()
        self.write(f"Level: {self.level_number}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)