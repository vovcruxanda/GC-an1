import turtle
from turtle import *

turtle.title('Flagul:Turcia, Vovc Ruxanda, TI-211')
setup(800,500)
bgcolor('#e5081a')
speed(0)

#moon shape
penup()
goto(-150, -135)
pendown()
begin_fill()
color('white')
circle(150)
end_fill()

penup()
goto(-120, -110)
pendown()
color('#e5081a')
begin_fill()
circle(130)
end_fill()

#star
penup()
goto(-50, 20)
pendown()
color('white')
begin_fill()
for i in range(5):
    forward(90)
    left(144)
end_fill()
done()
