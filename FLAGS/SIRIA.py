from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#cc0c24', outline='#cc0c24')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='black', outline='black')
centre_x=160
centre_y=130
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
panza.create_polygon(puncte, fill='#04843c', outline='#04843c')
centre_x1=260
centre_y1=130
R=25
puncte1 = [
    centre_x1 - int(R*m.sin(2*m.pi/5)),
    centre_y1 - int(R*m.cos(2*m.pi/5)),
    centre_x1 + int(R*m.sin(2*m.pi/5)),
    centre_y1 - int(R*m.cos(2*m.pi/5)),
    centre_x1 - int(R*m.sin(2*m.pi/10)),
    centre_y1 + int(R*m.cos(2*m.pi/10)),
    centre_x1 ,
    centre_y1 - R,
    centre_x1 + int(R*m.sin(2*m.pi/10)),
    centre_y1 + int(R*m.cos(2*m.pi/10)),
        ]
panza.create_polygon(puncte1, fill='#04843c', outline='#04843c')

panza.create_text(220,300,text='Flagul:Siria\nVovc Ruxanda\nTI-211', font='Helvetica 20')

