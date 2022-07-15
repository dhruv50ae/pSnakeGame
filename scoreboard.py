from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()