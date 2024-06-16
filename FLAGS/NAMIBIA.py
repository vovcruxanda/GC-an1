from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#05337c', outline='#05337c')
panza.create_polygon(40,230,380,20,380,230, fill='#04943e', outline='#04943e')
panza.create_polygon(380,20, 380,40, 80,230, 40,230, 40,210, 340,20, fill='white', outline='white')
panza.create_polygon(380,20, 380,35, 70,230, 40,230, 40,215, 350,20, fill='#d10c35', outline='#d10c35')
alfa=m.pi/12
x=90
y=120
r=23
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
panza.create_polygon(puncte, fill='#fbce01', outline='#fbce01')
panza.create_oval(95,65,145,115, fill='#05337c', outline='#05337c')
panza.create_oval(100,70,140,110, fill='#fbce01', outline='#fbce01')

panza.create_text(220,300,text='Flagul:Namibia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
