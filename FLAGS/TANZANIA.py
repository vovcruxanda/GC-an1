from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_polygon(40,20, 380,20, 40,230, fill='#1eb434', outline='#1eb434')
panza.create_polygon(380,230, 380,20, 40,230, fill='#05a4da', outline='#05a4da')
panza.create_polygon(380,20, 380,55, 100,230, 40,230, 40,195, 320,20, fill='#e7c811', outline='#e7c811')
panza.create_polygon(380,20, 380,40, 80,230, 40,230, 40,210, 340,20, fill='black', outline='black')


panza.create_text(220,300,text='Flagul:Tanzania\nVovc Ruxanda\nTI-211', font='Helvetica 20')
