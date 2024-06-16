from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Libia, Vovc Ruxanda, TI-211')

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

def rec(col,x,y):
    color(col)
    begin_fill()
    forward(x)
    left(90)
    forward(y)
    left(90)
    forward(x)
    end_fill()

def star(col,x):
    color(col)
    begin_fill()
    for i in range(5):
        forward(x)
        right(144)
    end_fill()

def drawmoon(x,y,col,radius):
    penup()
    goto(x,y)
    color(col)
    begin_fill()
    circle(radius)
    end_fill()

gt(-400,83)
rec("red",800,167)


left(180)

gt(-400,-251)
rec("#239e46",800,167)

left(180)

gt(-400,-125)
rec("black",800,250)

left(270)
drawmoon(20,0,"white",70)
drawmoon(26,0,"black",62)

gt(10,-40)
star("white",80)

hideturtle()
done()
