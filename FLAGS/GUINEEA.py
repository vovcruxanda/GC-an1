from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#cc0c24', outline='#cc0c24')
panza.create_rectangle(154,20,268,230, fill='#fcd40c', outline='#fcd40c')
panza.create_rectangle(268,20,382,230, fill='#049463', outline='#049463')
panza.create_text(250,300,text='Flagul:Guineea\nVovc Ruxanda\nTI-211', font='Helvetica 20')

