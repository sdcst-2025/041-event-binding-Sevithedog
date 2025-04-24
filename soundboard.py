import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p 
from PIL import Image, ImageTk

croc = Image.open("Bombardirocroc.png")
bomb = croc.resize((50,50))
tral = Image.open("Tralalero.png")
tralalero = tral.resize((50,50))
bannini = Image.open("Chimpanzini.png")
chimp = bannini.resize((50,50))
sahur = Image.open("Tung.png")
tungtung = sahur.resize((50,50))
lapol = Image.open("nonono.png")
policia = lapol.resize((50,50))



def playbomb(event):
    print(event)
    p.playsound("Voicy_Bombardino Crocodilo.mp3",block=False)
def playtral(event):
    print(event)
    p.playsound("tralalero-tralala-Meme-Sound.mp3",block=False)
def playchimp(event):
    print(event)
    p.playsound("chimpanzini-bananini.mp3",block=False)
def playtung(event):
    print(event)
    p.playsound("tung-tung-tung-tung-sahur.mp3",block=False)
def playno(event):
    print(event)
    p.playsound("lapolicia.mp3",block=False)
window = tk.Tk()
window.attributes('-topmost',True)
window.geometry("255x200")
#Labels
bomba = ImageTk.PhotoImage(bomb)
shark = ImageTk.PhotoImage(tralalero)
chimpanzee = ImageTk.PhotoImage(chimp)
tung = ImageTk.PhotoImage(tungtung)
nopolicia = ImageTk.PhotoImage(policia)


#Buttons
bombardirobt = tk.Button(window,image = bomba )
bombardirobt.bind("<Button>", playbomb)
tralbt = tk.Button(window, image = shark)
tralbt.bind("<Button>", playtral)
chimpbt = tk.Button(window, image = chimpanzee)
chimpbt.bind("<Button>", playchimp)
tungbt = tk.Button(window, image = tung)
tungbt.bind("<Button>", playtung)
policiabt = tk.Button(window, image = nopolicia)
policiabt.bind("<Button>", playno)


#Positioning
bombardirobt.place(x=0,y=50)
tralbt.place(x=50, y = 50)
chimpbt.place(x=100,y=50)
tungbt.place(x=150,y=50)
policiabt.place(x=200,y=50)
window.mainloop() 