from turtle import *
penup()
speed(5)
#F
setpos(-85,110) #centering in the screen
pendown()
pensize(10)
pencolor("gold3")
forward(100)
backward(100)
right(90)
forward(100)
left(90)
forward(70)
backward(70)
right(90)
forward(100)

backward(200)
left(90)
forward(100)
#C
#draw straight line
right(180)
circle(100,180)
#I
left(90)
forward(200)
#M
right(155)
forward(100)
left(135)
forward(100)
right(160)
forward(200)

backward(200)
right(20)
forward(100)
right(135)
forward(100)
left(65)
forward(100)
right(45)
forward(5)
right(135)

pencolor("gold")
forward(100)
backward(100)
right(90)
forward(100)
left(90)
forward(70)
backward(70)
right(90)
forward(100)

backward(200)
left(90)
forward(100)
#C
#draw straight line
right(180)
circle(100,180)
#I
left(90)
forward(200)
#M
right(155)
forward(100)
left(135)
forward(100)
right(160)
forward(200)




def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))
 
onscreenclick(buttonclick,1)
listen()  # listen to incoming connections
speed(10) # set the speed
done()



