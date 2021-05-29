from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0,-280)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(0,-280)



