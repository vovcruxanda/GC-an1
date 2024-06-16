from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,250,230, fill='#fb0404', outline='#fb0404')
panza.create_rectangle(128,60,162,190, fill='white', outline='white')
panza.create_rectangle(80,105,210,140, fill='white', outline='white')
panza.create_text(230,300,text='Flagul:Elvetia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

