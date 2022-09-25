from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color")
color = ["blue", "yellow", "red", "green", "cyan", "dark gray"]

y_position = [-150, -100, -50, 0, 50, 100, 150]

all_turtle = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-480, y=y_position[i])
    new_turtle.color(color[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}")
            else:
                print(f"You lost! The winning color is {winning_color}")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

# tommy = Turtle(shape="turtle")
# tommy.penup()
# tommy.goto(x=-480,y=-100)
# tommy.color("yellow")
#
# jerry = Turtle(shape="turtle")
# jerry.penup()
# jerry.goto(x=-480,y=-50)
# jerry.color("red")
#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(x=-480,y=0)
# tom.color("green")
#
# cather = Turtle(shape="turtle")
# cather.penup()
# cather.goto(x=-480,y=50)
# cather.color("purple")
#
# geni = Turtle(shape="turtle")
# geni.penup()
# geni.goto(x=-480,y=100)
# geni.color("cyan")
#
# maxy = Turtle(shape="turtle")
# maxy.penup()
# maxy.goto(x=-480,y=150)
# maxy.color("dark gray")


















screen.exitonclick()
