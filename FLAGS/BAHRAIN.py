from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#cc1424', outline='#cc1424')
y=0
for i in range(0,5):
    panza.create_polygon(40,20+y,120,20+y,160,41+y,120,62+y,40,62+y, fill='white', outline='white')
    y+=42
panza.create_text(250,300,text='Flagul:Bahrain\nVovc Ruxanda\nTI-211', font='Helvetica 20')

