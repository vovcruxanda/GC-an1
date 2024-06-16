from tkinter import *
window = Tk()
window.title('Laos')
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,75, fill='#ce1126', outline='#ce1126')
panza.create_rectangle(40,75,380,175, fill='#002868', outline='#002868')
panza.create_rectangle(40,175,380,230, fill='#ce1126', outline='#ce1126')
panza.create_oval(165,85,245,165, fill='white', outline='white')
panza.create_text(220,300,text='Flagul:Laos\nVovc Ruxanda\nTI-211', font='Helvetica 20')

