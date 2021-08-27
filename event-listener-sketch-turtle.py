import random
from turtle import Turtle, Screen

snake = Turtle()
screen = Screen()
screen.setup(height=500,width=500)
screen.bgcolor("black")
screen.title("Snaking")

snake.speed("slow")


food = Turtle()
food.speed("slow")
food.color("blue")
food.shape("circle")
food.shapesize(0.5,0.5)
food.penup()
food.goto(random.randint(-240,240),random.randint(-240,240))

size =1
snake.shapesize(0.5,1)

print(food.xcor())
print(food.ycor())

def right():
    snake.penup()
    global size
    if food.xcor() == snake.xcor() and food.ycor() == snake.ycor():
        size += 1
        snake.shapesize(0.5, size)
    snake.setheading(360)
    snake.forward(1);
def left():
    snake.penup()
    global size
    if food.xcor() == snake.xcor() and food.ycor() == snake.ycor():
        size += 1
        snake.shapesize(0.5, size)
    print(snake.xcor())
    snake.setheading(-180)
    snake.forward(1)
def up():
    snake.penup()
    global size

    if food.xcor() == snake.xcor() and food.ycor() == snake.ycor():
        size += 1
        snake.shapesize(0.5, size)
    print(snake.xcor())
    snake.setheading(90)
    snake.forward(1)
def down():
    snake.penup()
    global size
    if food.xcor() == snake.xcor() and food.ycor() == snake.ycor():
        size += 1
        snake.shapesize(0.5, size)
    print(snake.xcor())
    snake.setheading(-90)
    snake.forward(1)


screen.listen()
screen.onkey(fun=right,key="Right")
screen.onkey(fun=left,key="Left")
screen.onkey(fun=up,key="Up")
screen.onkey(fun=down,key="Down")

snake.color("white")
snake.shape("square")









screen.exitonclick()