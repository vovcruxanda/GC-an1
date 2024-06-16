from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#08428c', outline='#08428c')
panza.create_polygon(40,230,150,20,270,20, fill='#f7d656', outline='#f7d656')
panza.create_polygon(40,230,270,20,380,20,380,90, fill='#d91d1d', outline='#d91d1d')
panza.create_polygon(380,90,380,155,40,230, fill='white', outline='white')
panza.create_polygon(40,230,380,155,380,230, fill='#047b39', outline='#047b39')

panza.create_text(220,300,text='Flagul:Seychelles\nVovc Ruxanda\nTI-211', font='Helvetica 20')
