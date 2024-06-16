from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20, 380,230, fill='#059c46', outline='#059c46')
panza.create_polygon(40,20, 380,125, 40,230, fill='white', outline='white')
panza.create_polygon(40,30, 360,125, 40,220, fill='#f7d11c', outline='#f7d11c')
panza.create_polygon(40,20, 220,125, 40,230, fill='black', outline='black')
panza.create_polygon(40,32, 200,125, 40,218, fill='#ce0a22', outline='#ce0a22')

panza.create_text(220,300,text='Flagul:Guyana\nVovc Ruxanda\nTI-211', font='Helvetica 20')
