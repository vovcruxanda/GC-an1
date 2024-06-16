from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#049c64', outline='#049c64')
panza.create_rectangle(40,90,380,160, fill='#fcd40c', outline='#fcd40c')
panza.create_rectangle(40,160,380,230, fill='#3474c4', outline='#3474c4')
panza.create_text(250,300,text='Flagul:Gabon\nVovc Ruxanda\nTI-211', font='Helvetica 20')

