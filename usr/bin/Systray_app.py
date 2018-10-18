#!usr/bin/python
# Encoding : utf-8

'''
Test de script python en systray
'''


from pystray import MenuItem as item
import pystray
import time
import os
import webbrowser
from PIL import Image
import threading

class App():
    def __init__(self, *args):
        self.image = Image.open("python_icon.png")
        self.menu = pystray.Menu(item('Relancer script', self.Restart), item('Arrêter script', self.Stop), item('Configurer', self.Config), item('Quitter', self.Quit, default=True))
        self.icon = pystray.Icon("SFTP Uploader", self.image, 'SFTP Uploader', self.menu)

    def Code(self, stop_event, data):
        while not stop_event.wait(0.5):
            print('working with {}'.format(data))
        print('Thread stopped')

    def Start(self, *args):
        self.sentinel = threading.Event()
        self.t = threading.Thread(target=self.Code, args=(self.sentinel, "data"))
        self.t.start()

    def Stop(self, *args):
        self.sentinel.set()
        self.t.join()

    def Restart(self, *args):
        self.Stop()
        self.Start()
        

    def Config(self, *args):
        webbrowser.open("config.ini")
        print("User opened 'about' window")
        return

    def Quit(self, *args):
        self.Stop()
        self.icon.stop()

    def RunTray(self, *args):
        self.Start()
        self.icon.run()

if __name__ == '__main__':
    a = App()
    a.RunTray()
