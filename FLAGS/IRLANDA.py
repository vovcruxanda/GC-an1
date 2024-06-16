from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#169b62', outline='#169b62')
panza.create_rectangle(154,20,268,230, fill='white', outline='white')
panza.create_rectangle(268,20,382,230, fill='#fc8c3c', outline='#fc8c3c')
panza.create_text(250,300,text='Flagul:Irlanda\nVovc Ruxanda\nTI-211', font='Helvetica 20')

