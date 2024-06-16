from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#0544a9', outline='#0544a9')
panza.create_rectangle(154,20,268,230, fill='#f5ce0a', outline='#f5ce0a')
panza.create_rectangle(268,20,382,230, fill='#c90c2b', outline='#c90c2b')
panza.create_text(250,300,text='Flagul:Moldova\nVovc Ruxanda\nTI-211', font='Helvetica 20')

