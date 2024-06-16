from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,230, fill='#046cac', outline='#046cac')
panza.create_rectangle(145,20,185,230, fill='#facb05', outline='#facb05')
panza.create_rectangle(40,105,380,145, fill='#facb05', outline='#facb05')
panza.create_text(220,300,text='Flagul:Suedia\nVovc Ruxanda\nTI-211', font='Helvetica 20')

