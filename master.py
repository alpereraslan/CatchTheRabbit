import turtle
from random import randint
import time

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("green")
turtle_screen.title("Catch The Rabbit")
turtle_screen.addshape("/home/alperpc/İndirilenler/trying-pixel-art-for-first-time-16-bit-brown-rabbit-v0-aa7itywzxlga1.gif")
FONT = ("Arial", 30, "normal")

rabbit = turtle.Turtle()
score = turtle.Turtle()

score_value = 0

def setup_score():
    score.hideturtle()
    score.penup()

    score.color("black")
    score.setpos(0, 500)
    score.write(arg="Score: 0", move= False, align="center", font= FONT)

setup_score()

def rabbit_spawn(x, y):
    rabbit.teleport(x= randint(-850,850),y= randint(-650,650))
    handle_click(x, y)

def handle_click(x, y):
    global score_value
    score_value += + 1
    score.clear()
    score.write(arg="Score: {}".format(score_value), move=False, align="center", font=FONT)
    print(x, y)

countdown = turtle.Turtle()

def setup_countdown(time):
    countdown.hideturtle()
    countdown.penup()

    countdown.color("black")
    countdown.setpos(0, 460)
    countdown.clear()

    if time > 0:
        countdown.clear()
        countdown.write(arg="Time = {}".format(time), move=False, align="center", font=FONT)
        turtle_screen.ontimer(lambda: setup_countdown(time - 1),1000)
    else:
        countdown.clear()
        rabbit.hideturtle()
        countdown.write(arg="Game Over!", move=False, align="center", font=FONT)


setup_countdown(60)

rabbit.shape('/home/alperpc/İndirilenler/trying-pixel-art-for-first-time-16-bit-brown-rabbit-v0-aa7itywzxlga1.gif')
rabbit.penup()

rabbit.onclick(rabbit_spawn)

turtle.mainloop()