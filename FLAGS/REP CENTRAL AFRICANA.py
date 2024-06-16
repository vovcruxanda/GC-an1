from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,73, fill='darkblue', outline='darkblue')
panza.create_rectangle(40,73,380,126, fill='white', outline='white')
panza.create_rectangle(40,126,380,179, fill='green', outline='green')
panza.create_rectangle(40,179,380,232, fill='gold1', outline='gold1')
panza.create_rectangle(180,20,235,232, fill='red3', outline='red3')

centre_x=100
centre_y=47
R=26
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
panza.create_polygon(puncte, fill='#edc811', outline='#edc811')

panza.create_text(230,300,text='Flagul:Rep.Central Africana\nVovc Ruxanda\nTI-211', font='Helvetica 20')

