from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#008751', outline='#008751')
panza.create_rectangle(154,20,268,230, fill='white', outline='white')
panza.create_rectangle(268,20,382,230, fill='#008751', outline='#008751')
panza.create_text(250,300,text='Flagul:Nigeria\nVovc Ruxanda\nTI-211', font='Helvetica 20')

