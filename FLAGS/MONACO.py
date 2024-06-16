from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,135, fill='#cf0921', outline='#cf0921')
panza.create_rectangle(40,135,380,230, fill='white', outline='white')
panza.create_text(250,300,text='Flagul:Monaco\nVovc Ruxanda\nTI-211', font='Helvetica 20')
