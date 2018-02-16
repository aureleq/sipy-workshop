## This program scans for BLE devices and reports UID and RSSI values over Sigfox if
## "my_beacon" advertised name has been detected

import pycom
import binascii
import socket
from network import Sigfox, Bluetooth
from time import sleep

# name of the beacon to scan for
my_beacon = 'sigbeacon'

# function to send a sigfox message
# payload is of bytearray type
def sendSigfoxMessage(payload):
    # turn on RGB led
    pycom.rgbled(0x007f00)
    # create a Sigfox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
    # make the socket blocking
    s.setblocking(True)
    # configure it as uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
    # send some bytes
    s.send(payload)
    print("Message sent successfully!")
    s.close()
    # turn off RGB led
    pycom.rgbled(0x000000)


# run a BLE scan of "timeout" sec
# sends a sigfox message if a beacon with name "sigbeacon" is detected
def bleScan(timeout=3):
    print("NEW SCAN")
    bluetooth.start_scan(timeout)
    while bluetooth.isscanning():
        adv = bluetooth.get_adv()
        if adv:
            # print(binascii.hexlify(adv.data))
            # try to get the complete name
            ble_name = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)
            print("Name: ", ble_name, " RSSI: ", adv.rssi)
            if ble_name == my_beacon:
                # Location ID 16 bytes (ie: Eddystone UID) => 10 fixed bytes + 6 dedicated bytes per beacon
                location_uid = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_128SRV_CMPL)
                # display as hex format
                print("UID: ", binascii.hexlify(location_uid))
                # convert RSSI to 1 byte hex value, ie: -92 => 92 => 0x5C
                rssi_convert = binascii.unhexlify(hex(abs(adv.rssi))[2::])
                # send only 6 dedicated bytes (trim first 10 bytes)
                sendSigfoxMessage(location_uid[10::]+rssi_convert)



## main program

# disable RGB LED
pycom.heartbeat(False)
# initalise Sigfox for RCZ1 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
# print Sigfox Device ID
print("ID: ", binascii.hexlify(sigfox.id()))
# print Sigfox PAC number
print("PAC: ", binascii.hexlify(sigfox.pac()))

# init a new Bluetooth instance
bluetooth = Bluetooth()
# scan beacons every 30 sec
while True:
    sleep(30)
    bleScan(1)
