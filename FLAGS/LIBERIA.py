from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,245, fill='#c3052d', outline='#c3052d')
y = [40, 80, 120, 160, 200]
y1 = [60, 100, 140, 180, 220]
i=0
while i != len(y):
    panza.create_rectangle(40,y[i],380,y1[i], fill='white', outline='white')
    i+=1
panza.create_rectangle(40,20,150,119, fill='#07266c', outline='#07266c')
centre_x=95
centre_y=70
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

panza.create_text(220,300,text='Flagul:Liberia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
