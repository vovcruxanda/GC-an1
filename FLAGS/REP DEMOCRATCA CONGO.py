from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#047dfa', outline='#047dfa')
panza.create_polygon(380,20, 380,50, 95,230, 40,230, 40,200, 325,20, fill='#f5d81b', outline='#f5d81b')
panza.create_polygon(380,20, 380,40, 80,230, 40,230, 40,210, 340,20, fill='#c8111a', outline='#c8111a')
centre_x=110
centre_y=80
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
panza.create_polygon(puncte, fill='#f5d81b', outline='#f5d81b')

panza.create_text(220,300,text='Flagul:Rep. Democratica Congo\nVovc Ruxanda\nTI-211', font='Helvetica 14')
