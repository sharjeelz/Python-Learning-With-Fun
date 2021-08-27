from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.moves=0
        self.time=0
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f"Level {self.level} & Moves {self.moves}  & Time {self.time}",align="left")
    def clear_reset(self):
        self.clear()
        self.write(f"Level {self.level} & Moves {self.moves}  & Time {self.time}", align="left")
    def increase_level(self):
        self.level+=1
        self.clear_reset()
    def set_move(self, player_moves):

        self.clear()
        self.moves = player_moves
        self.write(f"Level {self.level} & Moves {self.moves}  & Time {self.time}", align="left")
    def set_time(self, time):
        self.clear()
        self.time=time
        self.write(f"Level {self.level} & Moves {self.moves} & Time {self.time}", align="left")






