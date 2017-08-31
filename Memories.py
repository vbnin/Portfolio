#python
# -*- coding: utf-8 -*-

"""
Ceci est un réceptacle de tous les morceaux de codes utiles dans Python :-)
"""

# Module pour pinger une plage d'adresses IP et lancer un thread pour chaque ping (progr asynchrone)
# for i in range(1,11):
#     hostname = "10.75.216.{0}".format(i)
#     t = threading.Thread(target=ping_machine,args=(hostname,))
#     t.start()
#     threads.append(t)
#     i += 1

# Check du type d'OS pour le cross platform
# def Op_Sys():
#     if platform.system().lower() == "windows":
#         return True
#     else:
#         return False

"""
Pour passer une variable au travers des fonctions et des fichiers, on utilise un dictionnaire :
c = {'counter' : 0}
c['counter'] = 1
print(['counter'])
"""