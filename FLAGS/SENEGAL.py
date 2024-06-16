from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#e4141c', outline='#e4141c')
panza.create_rectangle(154,20,268,230, fill='#f9f143', outline='#f9f143')
panza.create_rectangle(268,20,382,230, fill='#04843c', outline='#04843c')
centre_x=210
centre_y=130
R=40
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
panza.create_polygon(puncte, fill='#04843c', outline='#04843c')

panza.create_text(220,300,text='Flagul:Senegal\nVovc Ruxanda\nTI-211', font='Helvetica 20')

