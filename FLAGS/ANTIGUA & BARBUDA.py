from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Antigua & Barbuda, Vovc Ruxanda, TI-211')

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

def draw18star(size, col):
    speed(0)
    color(col)
    count = 0
    angle = 191
    ht()
    pu()
    pd()
    ht()
    right(26)
    begin_fill()
    speed(0)
    while count <= 15:
        forward(size)
        right(angle)
        count += 1
    end_fill()
    ht()

bgcolor("black")

gt(-185,105)
draw18star(400,'#f8d00e')

home()
gt(-400,-50)
rec('#0173ca',800,100)

right(180)
gt(-400,-250)
rec("white",800,200)

left(90)
color("#d00822")
begin_fill()
gt(-400,250)
fd(500)
left(90)
fd(400)
gt(-400,250)
end_fill()

right(90)
color("#d00822")
begin_fill()
gt(400,250)
fd(500)
right(90)
fd(400)
gt(400,250)
end_fill()



hideturtle()
done()
