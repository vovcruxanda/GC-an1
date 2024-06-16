from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#65ccfb', outline='#65ccfb')
panza.create_polygon(150,215,270,215,210,35, fill='white', outline='white')
panza.create_polygon(160,215,260,215,210,65, fill='black', outline='black')
panza.create_polygon(150,215,270,215,210,125, fill='#fcd015', outline='#fcd015')

panza.create_text(220,300,text='Flagul:Sf. Lucia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
