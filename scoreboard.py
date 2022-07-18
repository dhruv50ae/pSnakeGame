from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align = ALIGNMENT, font=FONT)

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.updateScoreboard()