from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,40,380,230, fill='#049cfb', outline='#049cfb')
panza.create_oval(120,80,250,200, fill='#f7fa07', outline='#f7fa07')
panza.create_text(250,300,text='Flagul:Palau\nVovc Ruxanda\nTI-211', font='Helvetica 20')

