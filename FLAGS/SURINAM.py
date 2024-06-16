from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#347c3c', outline='#347c3c')
panza.create_rectangle(40,60, 380,190, fill='white', outline='white')
panza.create_rectangle(40,80, 380,170, fill='#b40424', outline='#b40424')

centre_x=200
centre_y=129
R=50
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
panza.create_polygon(puncte, fill='#edc917', outline='#edc917')
panza.create_text(220,300,text='Flagul:Surinam\nVovc Ruxanda\nTI-211', font='Helvetica 20')
