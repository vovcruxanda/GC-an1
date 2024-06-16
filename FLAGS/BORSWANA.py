from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#6cacd4', outline='#6cacd4')
panza.create_rectangle(40,103,380,148, fill='white', outline='white')
panza.create_rectangle(40,110,380,140, fill='black', outline='black')
panza.create_text(250,300,text='Flagul:Boswana\nVovc Ruxanda\nTI-211', font='Helvetica 20')

