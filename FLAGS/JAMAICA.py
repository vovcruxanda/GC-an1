from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_polygon(40,20, 80,20, 380,210, 380,230, 340,230, 40,40, fill='#f5b61c', outline='#f5b61c')
panza.create_polygon(380,20, 380,40, 80,230, 40,230, 40,210, 340,20, fill='#f5b61c', outline='#f5b61c')
panza.create_polygon(80,20, 210,102, 340,20, fill='#07754a', outline='#07754a')
panza.create_polygon(80,230, 210,148, 340,230, fill='#07754a', outline='#07754a')
panza.create_polygon(40,40, 173,125, 40,210, fill='black', outline='black')
panza.create_polygon(380,40, 247,125, 380,210, fill='black', outline='black')
panza.create_text(220,300,text='Flagul:Jamaica\nVovc Ruxanda\nTI-211', font='Helvetica 20')
