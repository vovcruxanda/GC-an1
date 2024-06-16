from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#04738b', outline='#04738b')
panza.create_rectangle(40,90,380,160, fill='#f4c12e', outline='#f4c12e')
panza.create_polygon(40,20,210,125,40,230, fill='black', outline='black')
panza.create_text(250,300,text='Flagul:Cehia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

