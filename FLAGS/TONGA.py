from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#c10000', outline='#c10000')
panza.create_rectangle(40,20,180,125, fill='white', outline='white')
panza.create_rectangle(95,35,120,105, fill='#c10000', outline='#c10000')
panza.create_rectangle(70,58,145,83, fill='#c10000', outline='#c10000')
panza.create_text(250,300,text='Flagul:Tonga\nVovc Ruxanda\nTI-211', font='Helvetica 20')

