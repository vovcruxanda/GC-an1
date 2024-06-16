from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='black', outline='black')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='#009639', outline='#009639')
panza.create_polygon(40,20,200,240/2, 40, 230, outline='#ed2e38', fill='#ed2e38')

panza.create_text(220,300,text='Flagul:Palestina\nVovc Ruxanda\nTI-211', font='Helvetica 20')
