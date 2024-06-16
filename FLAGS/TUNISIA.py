from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul:Tunisia, Vovc Ruxanda, TI-211')

bgcolor('#e8000b')

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

def star(col,x):
    color(col)
    begin_fill()
    for i in range(5):
        forward(x)
        right(144)
    end_fill()

gt(-10,-100)
color("white")
begin_fill()
circle(100)
end_fill()

gt(-10,-80)
color("#e8000b")
begin_fill()
circle(80)
end_fill()

gt(13,-65)
color("white")
begin_fill()
circle(65)
end_fill()

left(20)
gt(-30,0)
star("#e8000b",90)

hideturtle()
done()
