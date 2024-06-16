from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#d81c20', outline='#d81c20')
panza.create_polygon(190,20,230,20,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(320,20,380,20,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(380,105,380,145,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(380,230,320,230,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(190,230,230,230,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(40,230,100,230,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(40,105,40,145,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_polygon(40,20,100,20,210,125, fill='#f9e32f', outline='#f9e32f')
panza.create_oval(180,95,240,155, fill='#d81c20', outline='#d81c20')
panza.create_oval(185,100,235,150, fill='#f9e32f', outline='#f9e32f')


panza.create_text(220,300,text='Flagul:Macedonia de Nord\nVovc Ruxanda\nTI-211', font='Helvetica 20')
