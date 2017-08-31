#python v3.6.1
# -*- coding: utf-8 -*-

import threading
import os
from utils.ressources import thread_ping
from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    csv_file = os.path.join(os.path.dirname(__file__), "Adresses_IP.csv")
    threads = []
    adresses_IP = []
    c = {'counter': 0, 'response' : False}
    total = 0

    with open(csv_file) as liste_ip:
        for row in liste_ip:
            adresses_IP.append(row.strip())
    liste_ip.close()

    for a in adresses_IP:
        hostname = a
        t = threading.Thread(target=thread_ping, args=(hostname, c))
        t.start()
        threads.append(t)
        total += 1
        if c['response'] is True:
            return("La machine {} est joignable.".format(hostname))
        else:
            return("La machine {} est injoignable !!".format(hostname))

    for t in threads:
        t.join()

    return("Il y a {0} machines joignables sur {1}.".format(c['counter'], total))