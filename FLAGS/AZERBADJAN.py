from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')

panza.create_rectangle(40,20,380,90, fill='#04b3e3', outline='#04b3e3')
panza.create_rectangle(40,90,380,160, fill='#ea3645', outline='#ea3645')
panza.create_rectangle(40,160,380,230, fill='#549b2c', outline='#549b2c')



panza.create_oval(180,91,260,159, fill='white', outline='white')
panza.create_oval(195,95,260,155, fill='#ea3645', outline='#ea3645')

alfa=m.pi/8
y=250
x=125
r=8
puncte = [

    y-2*r,
    x,

    y-r*m.cos(alfa),
    x+r*m.sin(alfa),

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

    y+r*m.cos(alfa),
    x+r*m.sin(alfa),

    y+2*r,
    x,

    y+r*m.cos(alfa),
    x-r*m.sin(alfa),

    y+2*r*m.cos(2*alfa),
    x-2*r*m.sin(2*alfa),

    y+r*m.sin(alfa),
    x-r*m.cos(alfa),

    y,
    x-2*r,

    y-r*m.sin(alfa),
    x-r*m.cos(alfa),

    y-2*r*m.sin(2*alfa),
    x-2*r*m.cos(2*alfa),

    y-r*m.cos(alfa),
    x-r*m.sin(alfa),
        ]
panza.create_polygon(puncte, fill='white', outline='white')

panza.create_text(220,300,text='Flagul:Azerbadjan\nVovc Ruxanda\nTI-211', font='Helvetica 20')
