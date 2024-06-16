from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,154,230, fill='#049444', outline='#049444')
panza.create_rectangle(154,20,268,230, fill='white', outline='white')
panza.create_rectangle(268,20,382,230, fill='#cc2c34', outline='#cc2c34')
panza.create_text(250,300,text='Flagul:Italia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

