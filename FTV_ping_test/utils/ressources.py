#python v3.6.1
# -*- coding: utf-8 -*-

import subprocess
import platform

system = "windows"

def Op_Sys():
    if platform.system().lower() == system:
        return True
    else:
        return False

def thread_ping(hostname, c):
    try:
        subprocess.check_output("ping -{0} 2 -w 300 -{1} 255 {2}".format("n" if Op_Sys() is True else "c", "i" if Op_Sys() is True else "t", hostname))
    except:
        print("La machine ", hostname, " est injoignable !!")
        return False
    c['counter'] += 1
    print("La machine ", hostname, " est joignable.")
    return True