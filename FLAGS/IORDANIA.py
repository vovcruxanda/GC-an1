import turtle
from turtle import *
turtle.title('Flagul: Iordania, Vovc Ruxanda, TI-211')
speed(0)
setup(1200,700)
penup()
goto(-400,250)

pendown()

fillcolor("black")
begin_fill()
forward(800)
right(90)
forward(166)
right(90)
forward(800)
right(90)
forward(166)
end_fill()
right(180)
fillcolor("#007a3d")
begin_fill()
forward(500)
left(90)
forward(800)
left(90)
forward(166)
left(90)
forward(800)
end_fill()
penup()
goto(-400,250)
pendown()
left(180)
color("#ce1126")
fillcolor("#ce1126")
begin_fill()
goto(-50,0)
goto(-400,-250)
goto(-400,250)
end_fill()
penup()
goto(-300,0)
pendown()
color("white")

def star():
    n = 7
    angle = 180 - 180 / n
    for i in range(n):
        forward(30)
        right(angle)

begin_fill()
star()
end_fill()

color("black")
penup()
goto(-400,250)
pendown()
goto(400,250)
goto(400,-250)
goto(-400,-250)


hideturtle()
turtle.done()
