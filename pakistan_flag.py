import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)
colors = [(1, 64, 27), (254, 254, 254)]
scree = Screen()
timmy = Turtle()
timmy.setheading(90)
timmy.forward(100)
timmy.color("black", "white")
timmy.begin_fill()
timmy.shape("square")
timmy.shapesize(10, 10, 1)
timmy.end_fill()


jimmy= Turtle()
jimmy.speed("fastest")
jimmy.forward(100)
jimmy.setheading(90)
jimmy.forward(100)
jimmy.color("black", colors[0])
jimmy.begin_fill()
jimmy.shape("square")
jimmy.shapesize(10, 10, 1)
jimmy.end_fill()


minny = Turtle()
minny.up()
minny.goto(90,50)
minny.color('white')
minny.begin_fill()
minny.circle(60)
minny.end_fill()
minny.up()
minny.goto(105,50)
minny.color(colors[0])
minny.begin_fill()
minny.circle(60)
minny.end_fill()
minny.up()
minny.goto(70,120)
minny.begin_fill()
minny.color("white")
for i in range(5):
    # moving turtle 100 units forward
    minny.forward(50)

    # rotating turtle 144 degree right
    minny.right(144)
minny.end_fill()


scree.exitonclick()
