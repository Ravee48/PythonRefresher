from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
x = -290
y = 150


for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=x, y=y)
    y -= +45
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# diff_tim()

screen.exitonclick()
