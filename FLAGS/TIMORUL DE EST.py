from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Timorul de Est, Vovc Ruxanda, TI-211')

bgcolor("#db2417")

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

def triangle(col,x,y,z):
    color(col)
    begin_fill()
    forward(x)
    left(y)
    forward(z)
    end_fill()
    right(y)

def star(col,x):
    color(col)
    begin_fill()
    for i in range(5):
        forward(x)
        right(144)
    end_fill()

gt(-400,250)
right(90)
triangle("#fec82b",500,125,450)
gt(-400,250)
triangle("black",500,136,350)

penup()
home()
pendown()

gt(-380,0)
left(20)
star("white",150)

hideturtle()
done()
