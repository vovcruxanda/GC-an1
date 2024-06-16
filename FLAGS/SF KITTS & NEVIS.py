from turtle import *
import time

speed(0)
setup(800,500)
title('Sf. Kitts & Nevis, Vovc Ruxanda, TI-211')
bgcolor("#009836")

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

gt(-400,-250)
color("#c9072a")
begin_fill()
gt(400,250)
gt(400,-250)
end_fill()

right(90)
color("gold")
gt(-400,-100)
begin_fill()
forward(150)
left(90)
forward(200)
left(90)
goto(400,100)
forward(150)
left(90)
forward(200)
goto(-400,-100)
end_fill()

left(90)
gt(-400,-150)
color("black")
begin_fill()
forward(100)
left(90)
forward(150)
left(90)
goto(400,140)
forward(110)
left(90)
forward(150)
goto(-400,-140)
end_fill()

right(5)
gt(-50,-115)
star("white",150)

gt(200,35)
star("white",150)

hideturtle()
done()
