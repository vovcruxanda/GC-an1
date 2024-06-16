from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#fbcc04', outline='#fbcc04')
panza.create_rectangle(40,90,380,160, fill='#39b334', outline='#39b334')
panza.create_rectangle(40,160,380,230, fill='#ec2434', outline='#ec2434')
centre_x=210
centre_y=130
R=80
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


panza.create_text(220,300,text='Flagul:Myanmar\nVovc Ruxanda\nTI-211', font='Helvetica 20')

