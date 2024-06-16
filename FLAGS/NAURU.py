from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#042c7c', outline='#042c7c')
panza.create_rectangle(40,115,380,135, fill='#f5c22e', outline='#f5c22e')

alfa=m.pi/12
y=130
x=170
r=15
puncte = [

    y-2*r,
    x,

    y-r*m.cos(alfa),
    x+r*m.sin(alfa),

    y-2*r*m.sin(4*alfa),
    x+2*r*m.cos(4*alfa),

    y-r*m.sin(3*alfa),
    x+r*m.cos(3*alfa),

    y-2*r*m.sin(2*alfa),
    x+2*r*m.cos(2*alfa),

    y-r*m.sin(alfa),
    x+r*m.cos(alfa),

    y,
    x+2*r,

    y+r*m.sin(alfa),
    x+r*m.cos(alfa),

    y+2*r*m.sin(2*alfa),
    x+2*r*m.cos(2*alfa),

    y+r*m.sin(3*alfa),
    x+r*m.cos(3*alfa),

    y+2*r*m.sin(4*alfa),
    x+2*r*m.cos(4*alfa),

    y+r*m.cos(alfa),
    x+r*m.sin(alfa),

    y+2*r,
    x,

    y+r*m.cos(alfa),
    x-r*m.sin(alfa),

    y+2*r*m.cos(2*alfa),
    x-2*r*m.sin(2*alfa),

    y+r*m.cos(3*alfa),
    x-r*m.sin(3*alfa),

    y+2*r*m.cos(4*alfa),
    x-2*r*m.sin(4*alfa),

    y+r*m.sin(alfa),
    x-r*m.cos(alfa),

    y,
    x-2*r,

    y-r*m.sin(alfa),
    x-r*m.cos(alfa),

    y-2*r*m.sin(2*alfa),
    x-2*r*m.cos(2*alfa),

    y-r*m.sin(3*alfa),
    x-r*m.cos(3*alfa),

    y-2*r*m.sin(4*alfa),
    x-2*r*m.cos(4*alfa),
    
    y-r*m.cos(alfa),
    x-r*m.sin(alfa),
        ]
panza.create_polygon(puncte, fill='white', outline='white')

panza.create_text(250,300,text='Flagul:Nauru\nVovc Ruxanda\nTI-211', font='Helvetica 20')
