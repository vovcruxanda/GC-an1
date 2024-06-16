from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,135, fill='#fcd404', outline='#fcd404')
panza.create_rectangle(40,125,380,173, fill='#042c8b', outline='#042c8b')
panza.create_rectangle(40,173,380,221, fill='#cb042c', outline='#cb042c')
panza.create_text(250,300,text='Flagul:Columbia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
