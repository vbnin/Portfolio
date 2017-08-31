#python v3.6.1
# -*- coding: utf-8 -*-

import subprocess
import platform
import threading
from time import sleep

system = "windows"
# threads = []

def color():
    global color
    color = "yellow"
    return color

def Op_Sys():
    if platform.system().lower() == system:
        return True
    else:
        return False

def thread_ping(hostname):
    try:
        subprocess.check_output("ping -{0} 2 -w 300 -{1} 255 {2}".format("n" if Op_Sys() is True else "c", "i" if Op_Sys() is True else "t", hostname))
    except:
        print("La machine ", hostname, " est injoignable !!")
        color = "red"
        return False
    print("La machine ", hostname, " est joignable.")
    color = "green"
    return True

def ping_action(IP):
    t = threading.Thread(target=thread_ping, args=(IP))
    t.start()
    t.join()
    # threads.append(t)
    # for t in threads:
    #     t.join()