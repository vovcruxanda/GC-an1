from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,125, fill='#6bb4ea', outline='#6bb4ea')
panza.create_rectangle(40,125, 380,230, fill='#0bac25', outline='#0bac25')
panza.create_polygon(40,20, 240,125, 40,230, fill='white', outline='white')

centre_x=110
centre_y=125
R=25
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
panza.create_polygon(puncte, fill='#da0d19', outline='#da0d19')

panza.create_text(220,300,text='Flagul:Djibouti\nVovc Ruxanda\nTI-211', font='Helvetica 20')
