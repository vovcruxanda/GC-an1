from tkinter import *
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#dc0c14', outline='#dc0c14')
panza.create_rectangle(90,70,330,180, fill='#067833', outline='#067833')
panza.create_oval(180,85,260,165, fill='white', outline='white')
panza.create_oval(200,85,280,165, fill='#067833', outline='#067833')

panza.create_text(220,300,text='Flagul:Maldive\nVovc Ruxanda\nTI-211', font='Helvetica 20')
