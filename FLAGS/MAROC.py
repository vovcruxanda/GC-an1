from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Maroc, Vovc RUxanda, TI-211')

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

bgcolor("#c1272d")

gt(-100,40)
color("#04492c")
width(10)
for i in range(5):
    forward(200)
    right(144)

done()
