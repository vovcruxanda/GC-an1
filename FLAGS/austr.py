from turtle import *
import time

speed(0)
setup(800,500)

bgcolor("#00008b")

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
def draw7star(size, col,rotate):
    speed(0)
    color(col)
    count = 0
    angle = 155
    ht()
    pu()
    pd()
    ht()
    left(rotate)
    begin_fill()
    speed(0)
    while count <= 5:
        forward(size)
        right(angle)
        count += 1
    end_fill()
    ht()


gt(-400,60)
color("white")
begin_fill()
gt(-400,0)
gt(0,220)
gt(0,250)
gt(-60,250)
gt(-400,60)
end_fill()


gt(-400,250)
color("white")
begin_fill()
gt(-400,190)
gt(-60,0)
gt(0,0)
gt(0,30)
gt(-400,250)
end_fill()

gt(-400,90)
rec("white",400,70)

left(180)
gt(-250,0)
rec("white",70,250)

left(180)
gt(-400,100)
rec("#ff0000",400,50)

left(180)
gt(-240,0)
rec("#ff0000",50,250)
#red

gt(-400,30)
color("#ff0000")
begin_fill()
gt(-400,5)
gt(-250,90)
gt(-290,90)
gt(-400,30)
end_fill()

gt(0,250)
color("#ff0000")
begin_fill()
gt(-50,250)
gt(-180,175)
gt(-140,175)
gt(0,250)
end_fill()

gt(-400,230)
color("#ff0000")
begin_fill()
gt(-400,200)
gt(-330,160)
gt(-290,160)
gt(-400,230)
end_fill()

gt(0,0)
color("#ff0000")
begin_fill()
gt(0,25)
gt(-120,90)
gt(-160,90)
gt(0,0)
end_fill()

gt(-140,-125)
draw7star(150,"white",1)

gt(300,125)
draw7star(50,"white",4)

gt(100,10)
draw7star(50,"white",4)

gt(200,200)
draw7star(50,"white",4)

gt(200,-200)
draw7star(50,"white",4)

penup()
home()
pendown()
gt(250,-20)
star("white",30)





hideturtle()
done()
