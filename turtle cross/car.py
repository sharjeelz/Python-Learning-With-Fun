import random
from turtle import Turtle

colors = ["red","orange","green","blue","yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
   def __init__(self):
      self.all_cars=[]
      self.car_speed = STARTING_MOVE_DISTANCE


   def create_car(self):
      random_chance = random.randint(1,6)
      if random_chance == 1:
         new_car = Turtle("square")
         new_car.shapesize(1, 2.5)
         new_car.penup()
         new_car.color(random.choice(colors))
         random_y = random.randint(-250,250)
         new_car.goto(300,random_y)
         self.all_cars.append(new_car)



   def level_up(self):
      self.car_speed += MOVE_INCREMENT
   def move(self):
      for car in self.all_cars:
         car.setheading(180)
         car.forward(MOVE_INCREMENT)



