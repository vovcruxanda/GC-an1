from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,236, fill='#8b0c34', outline='#8b0c34')
y=0
for i in range(0,9):
    panza.create_polygon(40,20+y,120,20+y,160,32+y,120,44+y,40,44+y, fill='white', outline='white')
    y+=24
panza.create_text(250,300,text='Flagul:Qatar\nVovc Ruxanda\nTI-211', font='Helvetica 20')

