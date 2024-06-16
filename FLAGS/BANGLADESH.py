from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,40,380,230, fill='#006a4e', outline='#006a4e')
panza.create_oval(110,70,240,200, fill='#f02c44', outline='#f02c44')
panza.create_text(250,300,text='Flagul:Bangladesh\nVovc Ruxanda\nTI-211', font='Helvetica 20')

