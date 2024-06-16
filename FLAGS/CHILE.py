from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,125, fill='white', outline='white')
panza.create_rectangle(40,125,380,230, fill='#d82719', outline='#d82719')
panza.create_rectangle(40,20,155,125, fill='#0434a4', outline='#0434a4')

centre_x=97
centre_y=72
R=26
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
panza.create_polygon(puncte, fill='white', outline='white')

panza.create_text(230,300,text='Flagul:Chile\nVovc Ruxanda\nTI-211', font='Helvetica 20')

