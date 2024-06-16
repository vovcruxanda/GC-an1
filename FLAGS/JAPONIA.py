from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,40,380,230, fill='white', outline='white')
panza.create_oval(145,80,275,200, fill='#bc002d', outline='#bc002d')
panza.create_text(250,300,text='Flagul:Japonia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

