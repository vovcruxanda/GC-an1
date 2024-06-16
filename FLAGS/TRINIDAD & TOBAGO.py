from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#db1434', outline='#db1434')
panza.create_polygon(40,20, 120,20, 380,230, 300,230, fill='white', outline='white')
panza.create_polygon(50,20, 110,20, 370,230, 310,230, fill='black', outline='black')

panza.create_text(220,300,text='Flagul:Trinidad & Tobago\nVovc Ruxanda\nTI-211', font='Helvetica 20')
