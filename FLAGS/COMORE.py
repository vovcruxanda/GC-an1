from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,73, fill='#fbd304', outline='#fbd304')
panza.create_rectangle(40,73,380,126, fill='white', outline='white')
panza.create_rectangle(40,126,380,179, fill='#e9343d', outline='#e9343d')
panza.create_rectangle(40,179,380,232, fill='#093da2', outline='#093da2')
panza.create_polygon(40,20,200,125,40,230, fill='#0c8930', outline='#0c8930')
panza.create_oval(50,75,150,175, fill='white', outline='white')
panza.create_oval(70,75,150,175, fill='#0c8930', outline='#0c8930')
i = 105
y = [90, 113, 135, 158]
for j in y:
    R=8
    puncte = [
        i - int(R*m.sin(2*m.pi/5)),
        j - int(R*m.cos(2*m.pi/5)),
        i + int(R*m.sin(2*m.pi/5)),
        j - int(R*m.cos(2*m.pi/5)),
        i - int(R*m.sin(2*m.pi/10)),
        j + int(R*m.cos(2*m.pi/10)),
        i ,
        j-R,
        i + int(R*m.sin(2*m.pi/10)),
        j + int(R*m.cos(2*m.pi/10)),
            ]
    panza.create_polygon(puncte, fill='white', outline='white')

panza.create_text(220,300,text='Flagul:Comore\nVovc Ruxanda\nTI-211', font='Helvetica 20')
