from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#cc0c24', outline='#cc0c24')
panza.create_rectangle(40,90,380,160, fill='#fad10c', outline='#fad10c')
panza.create_rectangle(40,160,380,230, fill='#056336', outline='#056336')

centre_x=210
centre_y=127
R=35
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
panza.create_polygon(puncte, fill='black', outline='black')

panza.create_text(220,300,text='Flagul:Ghana\nVovc Ruxanda\nTI-211', font='Helvetica 20')

