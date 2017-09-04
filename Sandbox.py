#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a quick sandbox used for testing parts of codes
"""

import re
import logging
from logging.handlers import RotatingFileHandler
from Libraries import ztest

handler = RotatingFileHandler('E:\PAR22_state.log', maxBytes=10000000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s : %(message)s'))
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(handler)

foo = "inutile = bar"
IPAddr = "1.2.3.4"

def HpaInfo(Nb, IPAddr, foo):
    Infos = {'Modele':foo,
             'Serial Number':foo,
             'Firmware':foo,
             'Total System Hours':foo,
             'Total Transmit Hours':foo,
             }
    logger.info("*** Spécifications du HPA #" + Nb + " ***")
    logger.info("Adresse IP : " + IPAddr)
    for key in Infos:
        m = re.search('(.*)\ =\ (.*)', Infos[key])
        if m is not None:
            logger.info(key + " : " + m.group(2))
    logger.info("***")

ztest()
HpaInfo('1', IPAddr, foo)
HpaInfo('2', IPAddr, foo)
