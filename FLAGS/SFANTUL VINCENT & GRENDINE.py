import turtle
from turtle import*
 
screen = turtle.Screen()
turtle.title()
t = turtle.Turtle()
speed(105)
 
t.penup()
t.goto(-300, 260)
t.pendown()
 
t.color('brown')
t.begin_fill()
t.forward(-10)
t.right(90)
t.forward(450)
t.right(90)
t.forward(-10)
t.end_fill()
t.right(90)
t.forward(450)
 
#Blue Rectangle
t.color('#002175')
t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(240)
t.right(90)
t.forward(100)
t.end_fill()
t.right(180)
t.forward(100)
 
#Yellow Rectangle
t.color('#fcd11c')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(240)
t.left(90)
t.forward(200)
t.end_fill()
t.left(180)
t.forward(200)
 
#Green Rectangle
t.color('#007d2a')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(240)
t.right(90)
t.forward(100)
t.end_fill()
 
#Diamond
t.penup()
t.goto(-130, 170)
t.pendown()
t.color('#007d2a')
t.begin_fill()
t.width(4)
t.left(60)
t.forward(40)
t.left(60)
t.forward(40)
t.left(120)
t.forward(40)
t.left(60)
t.forward(40)
t.end_fill()
 
####
t.penup()
t.goto(-77, 170)
t.pendown()
t.color('#007d2a')
t.begin_fill()
t.width(4)
t.left(120)
t.forward(40)
t.left(60)
t.forward(40)
t.left(120)
t.forward(40)
t.left(60)
t.forward(40)
t.end_fill()
 
####
t.penup()
t.goto(-104, 120)
t.pendown()
t.color('#007d2a')
t.begin_fill()
t.width(4)
t.left(120)
t.forward(40)
t.left(60)
t.forward(40)
t.left(120)
t.forward(40)
t.left(60)
t.forward(40)
t.end_fill()
 
 
t.penup()
t.color('#002175')
t.goto(-300, 260)

t.penup()
t.setposition(150, -200)
t.write('Flagul:Sfantul Vincent & Grenadine\nVovc Ruxanda\nTI-211', font='Helvetica 20', align="right")
 
turtle.done()
