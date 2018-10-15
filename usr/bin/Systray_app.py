#!usr/bin/python
# Encoding : utf-8

'''
Test de script python en systray
'''


from pystray import MenuItem as item
import pystray
import tkinter as tk
from PIL import Image



def Config():
    pass

def on_exit(about_window):
    about_window.destroy()

def About():
    # Opening popup window
    print("User opened 'about' window")
    about_window = tk.Tk()
    about_window.resizable(False, False)
    about_window.attributes("-topmost", True)
    about_window.title("A propos de SFTP Uploader")
    about_window.protocol("WM_DELETE_WINDOW", on_exit)
    about_window.mainloop()

    

def Quit():
    icon.stop()

image = Image.open("python_icon.png")
menu = pystray.Menu(item('Configurer', Config), item('A propos', About), item('Quitter', Quit, default=True))
icon = pystray.Icon("SFTP Uploader", image, 'SFTP Uploader', menu)

if __name__ == '__main__':
    icon.run()
