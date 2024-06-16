from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#27397e', outline='#27397e')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='#27397e', outline='#27397e')
centre_x=210 #260
centre_y=130 #155
R=10
puncte = [
    centre_x - int(R*m.sin(2*m.pi/5)),
    centre_y - int(R*m.cos(2*m.pi/5)),
    centre_x + int(R*m.sin(2*m.pi/5)),
    centre_y - int(R*m.cos(2*m.pi/5)),
    centre_x - int(R*m.sin(2*m.pi/10)),
    centre_y + int(R*m.cos(2*m.pi/10)),
    centre_x ,
    centre_y - R,
    centre_x + int(R*m.sin(2*m.pi/10)),
    centre_y + int(R*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte, fill='#27397e', outline='#27397e')
 
centre_x1=160
centre_y1=110
R1=10
puncte = [
    centre_x1 - int(R1*m.sin(2*m.pi/5)),
    centre_y1 - int(R1*m.cos(2*m.pi/5)),
    centre_x1 + int(R1*m.sin(2*m.pi/5)),
    centre_y1 - int(R1*m.cos(2*m.pi/5)),
    centre_x1 - int(R1*m.sin(2*m.pi/10)),
    centre_y1 + int(R1*m.cos(2*m.pi/10)),
    centre_x1 ,
    centre_y1 - R1,
    centre_x1 + int(R1*m.sin(2*m.pi/10)),
    centre_y1 + int(R1*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte, fill='#27397e', outline='#27397e')
 
centre_x2=160 
centre_y2=145
R2=10
puncte = [
    centre_x2 - int(R2*m.sin(2*m.pi/5)),
    centre_y2 - int(R2*m.cos(2*m.pi/5)),
    centre_x2 + int(R2*m.sin(2*m.pi/5)),
    centre_y2 - int(R2*m.cos(2*m.pi/5)),
    centre_x2 - int(R2*m.sin(2*m.pi/10)),
    centre_y2 + int(R2*m.cos(2*m.pi/10)),
    centre_x2 ,
    centre_y2 - R2,
    centre_x2 + int(R2*m.sin(2*m.pi/10)),
    centre_y2 + int(R2*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte, fill='#27397e', outline='#27397e')
 
centre_x3=260
centre_y3=110
R3=10
puncte = [
    centre_x3 - int(R3*m.sin(2*m.pi/5)),
    centre_y3 - int(R3*m.cos(2*m.pi/5)),
    centre_x3 + int(R3*m.sin(2*m.pi/5)),
    centre_y3 - int(R3*m.cos(2*m.pi/5)),
    centre_x3 - int(R3*m.sin(2*m.pi/10)),
    centre_y3 + int(R3*m.cos(2*m.pi/10)),
    centre_x3 ,
    centre_y3 - R3,
    centre_x3 + int(R3*m.sin(2*m.pi/10)),
    centre_y3 + int(R3*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte, fill='#27397e', outline='#27397e')
 
centre_x4=260
centre_y4=145
R4=10
puncte = [
    centre_x4 - int(R4*m.sin(2*m.pi/5)),
    centre_y4 - int(R4*m.cos(2*m.pi/5)),
    centre_x4 + int(R4*m.sin(2*m.pi/5)),
    centre_y4 - int(R4*m.cos(2*m.pi/5)),
    centre_x4 - int(R4*m.sin(2*m.pi/10)),
    centre_y4 + int(R4*m.cos(2*m.pi/10)),
    centre_x4 ,
    centre_y4 - R4,
    centre_x4 + int(R4*m.sin(2*m.pi/10)),
    centre_y4 + int(R4*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte, fill='#27397e', outline='#27397e')

panza.create_text(220,300,text='Flagul:Honduras\nVovc Ruxanda\nTI-211', font='Helvetica 20')
