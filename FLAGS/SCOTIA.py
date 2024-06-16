from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#055db5', outline='#055db5')
panza.create_polygon(40,20, 80,20, 380,210, 380,230, 340,230, 40,40, fill='white', outline='white')
panza.create_polygon(380,20, 380,40, 80,230, 40,230, 40,210, 340,20, fill='white', outline='white')

panza.create_text(220,300,text='Flagul:Scotia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
