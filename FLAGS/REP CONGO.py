from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_polygon(40,230,40,20,300,20, fill='#049444', outline='#049444')
panza.create_polygon(300,20,380,20,120,230,40,230, fill='#fbdb4b', outline='#fbdb4b')
panza.create_polygon(380,20,380,230,120,230, fill='#dc1534', outline='#dc1534')
panza.create_text(250,300,text='Flagul:Rep. Congo\nVovc Ruxanda\nTI-211', font='Helvetica 20')

