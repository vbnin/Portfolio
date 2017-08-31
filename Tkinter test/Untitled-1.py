from tkinter  import *
from time import sleep
import os
import threading

csv_file = os.path.join(os.path.dirname(__file__), "Adresses_IP.csv")
adresses_IP = []
labels = []

with open(csv_file) as liste_ip:
    for row in liste_ip:
        adresses_IP.append(row.strip())
liste_ip.close()

fenetre = Tk()
fenetre.title("test")
fenetre.config(bg="grey")
frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE).pack(padx=10, pady=10)
titre = Label(fenetre, text="Hello, World!!", bg="yellow").pack()

for a in adresses_IP:
    label = Label(frame1, text=a, bg="yellow")
    label.pack(padx=10, pady=10)
    labels.append(label)
    fenetre.update()

def loop():
    print(labels)
    sleep(1)
    for label in labels:
        label.config(bg="green")
        label.update()
    sleep(1)
    for label in labels:
        label.config(bg="red")
        label.update()

t = threading.Thread(target=loop())
t.start()

fenetre.mainloop()
