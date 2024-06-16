from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='black')
panza.create_rectangle(40,20,380,90, fill='#ec2c3c', outline='#ec2c3c')
panza.create_rectangle(40,90,380,160, fill='white', outline='white')
panza.create_rectangle(40,160,380,230, fill='#04a4dc', outline='#04a4dc')
panza.create_text(250,300,text='Flagul:Luxemburg\nVovc Ruxanda\nTI-211', font='Helvetica 20')

