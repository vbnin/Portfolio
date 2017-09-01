#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a quick sandbox used for testing parts of codes
"""

import re
import logging

foo = "inutile = bar"
IPAddr = "1.2.3.4"

def log(level, msg):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
    logger = logging.getLogger(__name__)
    if level == "debug":
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    else:
        logger.error(msg)

def HpaInfo(Nb, IPAddr, foo):
    Infos = {'Modele':foo,
             'Serial Number':foo,
             'Firmware':foo,
             'Total System Hours':foo,
             'Total Transmit Hours':foo,
             }
    log("info", "*** Spécifications du HPA #" + Nb + " ***")
    log("info", "Adresse IP : " + IPAddr)
    for key in Infos:
        m = re.search('(.*)\ =\ (.*)', Infos[key])
        if m is not None:
            log("info", key + " : " + m.group(2))
    log("info", "***")

HpaInfo('1', IPAddr, foo)
HpaInfo('2', IPAddr, foo)
