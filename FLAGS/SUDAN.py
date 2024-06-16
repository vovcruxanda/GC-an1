from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#d31434', outline='#d31434')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='black', outline='black')
panza.create_polygon(40,20,140,125,40,230, fill='#087230', outline='#087230')
panza.create_text(220,300,text='Flagul:Sudan\nVovc Ruxanda\nTI-211', font='Helvetica 20')
