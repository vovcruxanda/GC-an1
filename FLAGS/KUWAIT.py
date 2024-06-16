from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#047b3b', outline='#047b3b')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='#cc0f26', outline='#cc0f26')
panza.create_polygon(40,20, 130,90, 130,160, 40,230, fill='black', outline='black')
panza.create_text(220,300,text='Flagul:Kuwait\nVovc Ruxanda\nTI-211', font='Helvetica 20')
