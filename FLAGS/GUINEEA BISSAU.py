from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,160,230, fill='#cb1717', outline='#cb1717')
panza.create_rectangle(160,20,380,125, fill='#fbd30c', outline='#fbd30c')
panza.create_rectangle(160,125,380,230, fill='#049c44', outline='#049c44')
centre_x=95
centre_y=125
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

panza.create_text(250,300,text='Flagul:Guineea-Bissau\nVovc Ruxanda\nTI-211', font='Helvetica 20')
