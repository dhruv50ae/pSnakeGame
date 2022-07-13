from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

startingPositions = [(0,0), (-20, 0), (-40, 0)]

for position in startingPositions:
    newSeg = Turtle("square")
    newSeg.color("white")
    newSeg.goto(position)

segOne = Turtle("square")
segOne.color("white")

segTwo = Turtle("square")
segTwo.color("white")
segTwo.goto(-20, 0)

segThree = Turtle("square")
segThree.color("white")
segThree.goto(-40, 0)

screen.exitonclick()
