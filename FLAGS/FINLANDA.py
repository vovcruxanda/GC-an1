from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='white', outline='white')
panza.create_rectangle(135,20,185,230, fill='#043484', outline='#043484')
panza.create_rectangle(40,100,380,150, fill='#043484', outline='#043484')
panza.create_text(220,300,text='Flagul:Finlanda\nVovc Ruxanda\nTI-211', font='Helvetica 20')

