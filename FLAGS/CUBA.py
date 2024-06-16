from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#042b8b', outline='#042b8b')
panza.create_rectangle(40,62, 380,104, fill='white', outline='white')
panza.create_rectangle(40,146, 380,188, fill='white', outline='white')
panza.create_polygon(40,20, 190,125, 40,230, fill='#cb1717', outline='#cb1717')
centre_x=90
centre_y=125
R=30
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

panza.create_text(220,300,text='Flagul:Cuba\nVovc Ruxanda\nTI-211', font='Helvetica 20')
