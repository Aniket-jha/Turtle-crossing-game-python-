import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for no_of_car in car.all_cars :
        if player.distance(no_of_car) <40 :
            player.reset_position()

        if player.ycor() > 280 and player.distance(no_of_car) > 40:
            player.reset_position()
            scoreboard.point()
            car.move_fast()













screen.exitonclick()







