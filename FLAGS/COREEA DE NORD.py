from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#044ca4', outline='#044ca4')
panza.create_rectangle(40,50, 380,200, fill='white', outline='white')
panza.create_rectangle(40,55, 380,195, fill='#ec1c24', outline='#ec1c24')
panza.create_oval(120,70, 230,180, fill='white', outline='white')
centre_x=175
centre_y=125
R=55
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
panza.create_polygon(puncte, fill='#ec1c24', outline='#ec1c24')
panza.create_text(220,300,text='Flagul:Coreea de Nord\nVovc Ruxanda\nTI-211', font='Helvetica 20')
