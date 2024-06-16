from turtle import *
import time

speed(0)
setup(800,500)
title('Flagul: Regatul Unit al Marii Britanii, Vovc Ruxanda, TI-211')

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

bgcolor("#001b69")

gt(-400,-75)
rec("white",800,150)

left(180)

gt(-75,-250)
rec("white",150,500)


gt(-400,250)
color("white")
begin_fill()
gt(-400,200)
gt(300,-250)
gt(400,-250)
gt(400,-200)
gt(-300,250)
gt(-400,250)
end_fill()

gt(-400,-250)
color("white")
begin_fill()
gt(-300,-250)
gt(400,200)
gt(400,250)
gt(300,250)
gt(-400,-200)
gt(-400,-250)
end_fill()

gt(-400,250)
color("#c9072a")
begin_fill()
gt(-400,210)
gt(-190,75)
gt(-140,75)
gt(-400,250)
end_fill()

gt(-400,-250)
color("#c9072a")
begin_fill()
gt(-320,-250)
gt(-75,-80)
gt(-130,-80)
gt(-400,-250)
end_fill()

gt(400,250)
color("#c9072a")
begin_fill()
gt(320,250)
gt(75,90)
gt(130,90)
gt(400,250)
end_fill()

gt(400,-250)
color("#c9072a")
begin_fill()
gt(400,-210)
gt(190,-75)
gt(140,-75)
gt(400,-250)
end_fill()

#red

penup()
home()
pendown()

gt(-400,-50)
rec("#c9072a",800,100)

left(180)

gt(-50,-250)
rec("#c9072a",100,500)


hideturtle()
done()
