from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#002164', outline='#002164')
panza.create_rectangle(154,20,268,230, fill='#fecc00', outline='#fecc00')
panza.create_rectangle(268,20,382,230, fill='#c7042c', outline='#c7042c')
panza.create_text(250,300,text='Flagul:Ciad\nVovc Ruxanda\nTI-211', font='Helvetica 20')

