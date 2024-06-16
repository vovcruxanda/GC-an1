from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Izrael, Vovc Ruxanda, TI-211')

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

gt(-400,-250)
rec("#0035b9",800,90)

right(180)

gt(-400,160)
rec("#0035b9",800,90)

gt(60,40)
color("#0035b9")
width(10)
forward(150)
left(120)
forward(150)
left(120)
forward(150)

right(240)
left(180)

gt(-90,-40)
color("#0035b9")
width(10)
forward(150)
left(120)
forward(150)
left(120)
forward(150)

done()
