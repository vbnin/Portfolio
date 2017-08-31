#!/usr/bin/env python
# -*- coding: utf-8 -*-
# v1.1 - 02/08/17 - vbnin

import RPi.GPIO as GPIO
import time
import telnetlib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

HPA1 = "10.191.100.41"
HPA2 = "10.191.100.42"
PSWD = "CPE=1234"
TRANSMIT = "TST"
QUIT = "DCN"
enabled = "1"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
HPA1_XMIT = 7
HPA2_XMIT = 25
GPIO.setup(HPA1_XMIT, GPIO.OUT)
GPIO.setup(HPA2_XMIT, GPIO.OUT)

time.sleep(10)

def loop():
	logger.info('Verifying XMIT status for HPA1 :')
	tn = telnetlib.Telnet(HPA1)
	tn.write(PSWD + "\r\n")
	tn.read_until(">")
	tn.write(TRANSMIT + "\r\n")
	tn.read_until("TST=")
	tn.close()
	state_HPA1 = tn.read_very_eager()
	logger.info(state_HPA1[3:])
	
	logger.info('Verifying XMIT status for HPA2 :')
	tn = telnetlib.Telnet(HPA2)
	tn.write(PSWD + "\r\n")
	tn.read_until(">")
	tn.write(TRANSMIT + "\r\n")
	tn.read_until("TST=")
	tn.close()
	state_HPA2 = tn.read_very_eager() 
	logger.info(state_HPA2[3:])

	if state_HPA1[:1] == enabled:
		GPIO.output(HPA1_XMIT, True)
		logger.debug("LED HPA1 allumee")
	else:
		GPIO.output(HPA1_XMIT, False)
		logger.debug("LED HPA1 eteinte")

	if state_HPA2[:1] == enabled:
		GPIO.output(HPA2_XMIT, True)
		logger.debug("LED HPA2 allumee" + "\n")
	else:
		GPIO.output(HPA2_XMIT, False)
		logger.debug("LED HPA2 eteinte" + "\n")

	time.sleep(4)

if __name__ == '__main__':
	try:
		logger.info("Press Ctrl+C to quit." + "\n")
		while True:
			loop()
	finally:
		GPIO.cleanup()