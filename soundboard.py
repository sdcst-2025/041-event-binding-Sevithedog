import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p 
from PIL import Image, ImageTk

croc = Image.open("Bombardirocroc.png")
bomb = croc.resize((50,50))
tral = Image.open("Tralalero.png")
tralalero = tral.resize((50,50))

def playbomb(event):
    print(event)
    p.playsound("Voicy_Bombardino Crocodilo.mp3")
def playtral(event):
    print(event)
    p.playsound("tralalero-tralala-Meme-Sound.mp3")

window = tk.Tk()
#Labels
bomba = ImageTk.PhotoImage(bomb)
shark = ImageTk.PhotoImage(tralalero)
#bombardirolb = tk.Label(window, image = phbomb)


#Buttons
bombardirobt = tk.Button(window,image = bomba )
bombardirobt.bind("<Button>", playbomb)
tralbt = tk.Button(window, image = shark)
tralbt.bind("<Button>", playtral)
#Positioning
bombardirobt.place(x=0,y=50,width = 50, height = 50)
tralbt.place(x=50, y = 50)
window.mainloop() 