from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#a6122d', outline='#a6122d')
panza.create_rectangle(40,55,380,195, fill='white', outline='white')
panza.create_rectangle(40,90,380,160, fill='#2a2349', outline='#2a2349')

panza.create_text(250,300,text='Flagul:Tailanda\nVovc Ruxanda\nTI-211', font='Helvetica 20')

