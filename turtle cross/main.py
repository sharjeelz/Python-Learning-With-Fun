from turtle import Screen
import time
from scoreboard import ScoreBoard
import car
from player import Player

from car import Car

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

score = ScoreBoard()



p1 = Player()





screen.listen()

screen.onkey(fun=p1.move,key="Up")

is_game_on = True
new_car = Car()
while is_game_on:
    start_time = time.time()
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move()

    for car in new_car.all_cars:
        if car.distance(p1) < 20:
            is_game_on = False
            score.goto(0,0)
            score.write("GameOver")


    if p1.is_at_finish_line():

        p1.goto_start()
        new_car.level_up()
        score.increase_level()
        score.set_move(p1.get_current_moves())
        score.set_time(time.time() - start_time)



screen.exitonclick()