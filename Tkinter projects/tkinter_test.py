#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import os
import threading
from utils.ressources_tkinter import Op_Sys
from time import sleep
import subprocess

fenetre = Tk()
fenetre.title("test")
csv_file = os.path.join(os.path.dirname(__file__), "Adresses_IP.csv")
adresses_IP = []
labels =[]

with open(csv_file) as liste_ip:
    for row in liste_ip:
        adresses_IP.append(row.strip())
liste_ip.close()

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=10, pady=10) 

for a in adresses_IP:
    label = Label(Frame1, text=a, bg="yellow")
    label.pack(padx=10, pady=10)
    labels.append(label)
    fenetre.update()

def action(adresses_IP, labels):
    for a, label in zip(adresses_IP, labels):
        try:
            subprocess.check_output("ping -{0} 2 -w 300 -{1} 255 {2}".format("n" if Op_Sys() is True else "c", "i" if Op_Sys() is True else "t", a))
            label.config(bg="green")
            fenetre.update()
        except:
            label.config(bg="red")
            fenetre.update()
    sleep(5)

while True:
    t = threading.Thread(target=action(adresses_IP, labels))
    t.start

fenetre.mainloop()
