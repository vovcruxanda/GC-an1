from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#04732c', outline='#04732c')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='black', outline='black')
panza.create_rectangle(40,20,120,230, fill='#fb0404', outline='#fb0404')
panza.create_text(220,300,text='Flagul:Emiratele Arabe Unite\nVovc Ruxanda\nTI-211', font='Helvetica 20')

