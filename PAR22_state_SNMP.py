from pysnmp.hlapi import *
import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
HPA1_XMIT = 7
HPA2_XMIT = 25
GPIO.setup(HPA1_XMIT, GPIO.OUT)
GPIO.setup(HPA2_XMIT, GPIO.OUT)
HPA1 = '10.75.216.60'
HPA2 = '10.75.216.61'
OID = '1.3.6.1.4.1.27338.4.15.4.2.2.2.2.2.1.1.6.1.1'

time.sleep(10)

def SNMPget(hostname, OID, HPAx_XMIT):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'),
            UdpTransportTarget((hostname, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID)))
    )

    if errorIndication:
        logger.error(errorIndication)
    elif errorStatus:
        logger.error('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            state = (' = '.join([x.prettyPrint() for x in varBind]))
            logger.debug(state)
            if state[-1:] == "1" and GPIO.output(HPAx_XMIT) is False:
                logger.info("LED " + hostname + " allumee")
                GPIO.output(HPAx_XMIT, True)
            elif state[-1:] == "1" and GPIO.output(HPAx_XMIT) is True:
                pass
            else:
                logger.info("LED " + hostname + " eteinte")
                GPIO.output(HPAx_XMIT, False)
  
def loop():
    SNMPget(HPA1, OID, HPA1_XMIT)
    time.sleep(1)
    SNMPget(HPA2, OID, HPA2_XMIT)
    time.sleep(1)

if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
	    GPIO.cleanup()