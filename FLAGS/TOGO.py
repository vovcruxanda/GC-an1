from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#066a4b', outline='#066a4b')
panza.create_rectangle(40,62, 380,104, fill='#fbcc04', outline='#fbcc04')
panza.create_rectangle(40,146, 380,188, fill='#fbcc04', outline='#fbcc04')
panza.create_rectangle(40,20, 166,146, fill='#d30634', outline='#d30634')
centre_x=100
centre_y=85
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
panza.create_polygon(puncte, fill='white', outline='white')

panza.create_text(220,300,text='Flagul:Togo\nVovc Ruxanda\nTI-211', font='Helvetica 20')
