from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='black')
panza.create_rectangle(40,20,160,230, fill='#008850', outline='#008850')
panza.create_rectangle(160,20,380,125, fill='#fcd20f', outline='#fcd20f')
panza.create_rectangle(160,125,380,230, fill='#e90929', outline='#e90929')
panza.create_text(250,300,text='Flagul:Benin\nVovc Ruxanda\nTI-211', font='Helvetica 20')
