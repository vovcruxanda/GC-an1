from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#0c745c', outline='#0c745c')
panza.create_rectangle(154,20,268,230, fill='#cb0e23', outline='#cb0e23')
panza.create_rectangle(268,20,382,230, fill='#fcd20f', outline='#fcd20f')

centre_x=210
centre_y=125
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
panza.create_polygon(puncte, fill='#edc811', outline='#edc811')

panza.create_text(250,300,text='Flagul:Camerun\nVovc Ruxanda\nTI-211', font='Helvetica 20')

