import tkinter as tk
import urllib.request
from PIL import ImageTk, Image
import Deck_generator as dk

User = int(input("Enter 1 for completely random deck, and 2 for a random deck with optimal card levels for path of legends: "))
if User == 1:
    img_urls=dk.randomDeck()[1]
elif User == 2:
    img_urls=dk.optimalDeck()[1]

ids=[]
for i in range(8):
    urllib.request.urlretrieve(f'{img_urls[i]}',
    f"c{i+1}.png")
    ids.append(f"c{i+1}.png")

root = tk.Tk()
imgs=[]
flag=False
for i in range(8):
    imgs.append(ImageTk.PhotoImage(Image.open(f"{ids[i]}")))
    tk.Label(root, image=imgs[i], width=277, height=330).grid(row=int(flag),column=i//2)
    flag=not flag
    
root.wm_title("Clash Helper")
root.geometry("1150x700")
root.mainloop()