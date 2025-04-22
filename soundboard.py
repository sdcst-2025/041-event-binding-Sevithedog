import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p 

def playbomb(event):
    print(event)
    p.playsound("Bombardiro.jpg")

window = tk.Tk()
#Labels
phbomb = tk.PhotoImage(file = "Bombardiro_Crocodilo.webp")
bombardirolb = tk.Label(window, image = phbomb)


#Buttons
bombardirobt = tk.Button()

#Positioning
