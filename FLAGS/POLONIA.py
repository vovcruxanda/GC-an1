from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,135, fill='white', outline='white')
panza.create_rectangle(40,135,380,230, fill='#dd0c39', outline='#dd0c39')
panza.create_text(250,300,text='Flagul:Polonia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
