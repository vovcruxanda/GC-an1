from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,90, fill='#fcbc14', outline='#fcbc14')
panza.create_rectangle(40,90,380,160, fill='#046c44', outline='#046c44')
panza.create_rectangle(40,160,380,230, fill='#c4242c', outline='#c4242c')
panza.create_text(250,300,text='Flagul:Lituania\nVovc Ruxanda\nTI-211', font='Helvetica 20')

