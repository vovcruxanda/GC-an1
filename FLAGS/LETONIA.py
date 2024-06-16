from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,135, fill='#9e3039', outline='#9e3039')
panza.create_rectangle(40,105,380,155, fill='white', outline='white')
panza.create_rectangle(40,145,380,230, fill='#9e3039', outline='#9e3039')
panza.create_text(250,300,text='Flagul:Letonia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
