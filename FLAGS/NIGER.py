from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,250,90, fill='#e45404', outline='#e45404')
panza.create_rectangle(40,90,250,160, fill='white', outline='white')
panza.create_rectangle(40,160,250,230, fill='#0db42d', outline='#0db42d')
panza.create_oval(115,95,175,155,fill='#e45404', outline='#e45404')
panza.create_text(220,300,text='Flagul:Niger\nVovc Ruxanda\nTI-211', font='Helvetica 20')

