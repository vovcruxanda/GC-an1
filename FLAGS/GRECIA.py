from tkinter import *
import math as m
window = Tk()
panza = Canvas(window, width=400, height=400)
panza.pack()
panza.create_rectangle(20,20,40,380, fill='brown', outline='brown')
panza.create_rectangle(40,20,380,245, fill='#045cb4', outline='#045cb4')
y = [45, 95, 145, 195]
y1 = [70, 120, 170, 220]
i=0
while i != len(y):
    panza.create_rectangle(40,y[i],380,y1[i], fill='white', outline='white')
    i+=1
panza.create_rectangle(40,20,180,144, fill='#045cb4', outline='#045cb4')
panza.create_rectangle(95,20,120,145, fill='white', outline='white')
panza.create_rectangle(40,70,180,95, fill='white', outline='white')

panza.create_text(220,300,text='Flagul:Grecia\nVovc Ruxanda\nTI-211', font='Helvetica 20')
