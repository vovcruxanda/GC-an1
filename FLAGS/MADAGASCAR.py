from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,150,230, fill='white', outline='white')
panza.create_rectangle(150,20,380,125, fill='red', outline='red')
panza.create_rectangle(150,125,380,230, fill='green', outline='green')
panza.create_text(250,300,text='Flagul:Madagascar\nVovc Ruxanda\nTI-211', font='Helvetica 20')

