from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)
        self.moves=0

    def goto_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def move(self):
        self.forward(MOVE_DISTANCE)
        self.moves+=1

    def get_current_moves(self):
        return self.moves

