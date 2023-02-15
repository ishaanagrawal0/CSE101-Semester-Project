import tkinter as tk
import urllib.request
from PIL import ImageTk, Image


urllib.request.urlretrieve(
  'https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png',
   "c1.png")
urllib.request.urlretrieve(
  'https://api-assets.clashroyale.com/cards/300/W4Hmp8MTSdXANN8KdblbtHwtsbt0o749BbxNqmJYfA8.png',
   "c2.png")

  
# img = Image.open("gfg.png")
# img.show()
root = tk.Tk()


ids = ["c1.png","c2.png"]
imgs=[]
for i in range(len(ids)):
    imgs.append(ImageTk.PhotoImage(Image.open(f"{ids[i]}")))
    tk.Label(root, image=imgs[-1], width=277, height=330).grid()

root.mainloop()