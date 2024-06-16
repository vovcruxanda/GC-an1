from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#bc042c', outline='#bc042c')
panza.create_rectangle(135,20,185,230, fill='white', outline='white')
panza.create_rectangle(40,100,380,150, fill='white', outline='white')
panza.create_rectangle(145,20,175,230, fill='#081f5b', outline='#081f5b')
panza.create_rectangle(40,110,380,140, fill='#081f5b', outline='#081f5b')

panza.create_text(220,300,text='Flagul:Norvegia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

