from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='red1', outline='red1')
panza.create_rectangle(40,90,380,160, fill='darkblue', outline='darkblue')
panza.create_rectangle(40,160,380,230, fill='gold', outline='gold')
panza.create_text(250,300,text='Flagul:Armenia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

