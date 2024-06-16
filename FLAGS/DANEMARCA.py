from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#c4042c', outline='#c4042c')
panza.create_rectangle(155,20,185,230, fill='white', outline='white')
panza.create_rectangle(40,105,380,140, fill='white', outline='white')
panza.create_text(230,300,text='Flagul:Danemarca\nVovc Ruxanda\nTI-211', font='Helvetica 20')

