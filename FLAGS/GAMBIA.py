from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,125, fill='#cc0c24', outline='#cc0c24')
panza.create_rectangle(40,125,380,230, fill='#347c24', outline='#347c24')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,100,380,150, fill='#04148c', outline='#04148c')
panza.create_text(220,300,text='Flagul:Gambia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

