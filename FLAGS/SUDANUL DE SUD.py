from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul:Sudanul de Sud, Vovc Ruxanda, TI-211')

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

def triangle(col,x,y,z):
    color(col)
    begin_fill()
    forward(x)
    left(y)
    forward(z)
    end_fill()
    right(y)

gt(-400,-250)
rec("#078930",800,156.6)

left(180)

gt(-400,-78.3)
rec("#da121a",800,156.6)

left(180)

gt(-400,94)
rec("black",800,156.6)

gt(-400,250)
left(90)
triangle("#0f47af",500,130,400)

gt(-310,77)
left(35)
star("#fcdd09",150)


hideturtle()
done()
