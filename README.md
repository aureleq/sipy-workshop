# sipy-workshop

## Introduction
This repository contains examples to get started with Sigfox and SiPy board.

## How to use Sigfox during the workshop
Development Kits from Pycom will be provided (https://www.pycom.io/product/sipy/) with free premium subscription (140 uplink messages/day + 4 downlink/day). Teams will be able to activate their sigfox account using the following link: https://backend.sigfox.com/activate/

To get started with Sigfox you can follow the guide online: http://makers.sigfox.com/getting-started/

Pycom documentation is available here: https://docs.pycom.io/chapter/gettingstarted/

## Prerequisite
Install atom and the pymakr plugin as explained here: https://docs.pycom.io/chapter/gettingstarted/installingsoftware.html

You can connect to the board using the serial port. In the pymakr console, click *more* and then *get serial ports*. Select the SiPy serial port and copy it in *Global Settings* => *Device Address*. Click *Reconnect* in the pymakr console to access the board.


## Examples
- example-sigfox/sigfox-helloworld.py

  Shows how to send your first sigfox message. It also displays your board ID and PAC that are required to register your dev kit on sigfox backend (https://backend.sigfox.com/activate/)
  Open the file and click *Run* to start the program.

- example/sigfox/sigfox-downlink.py

  Sends a sigfox message and requests an acknowledgement from the network. Content of the Ack can be customized on the sigfox backend or on your application server (callbacks mechanism)

- example-ble-sigfox

  This program scans for BLE devices and reports UID and RSSI values over Sigfox if "my_beacon" advertised name has been detected.

  You can use the Sync button to flash the board as it contains the boot.py and main.py files. First click *Project Settings* and set the sync folder as "example-ble-sigfox". Click *Sync* to flash the board with the boot.py and main.py files. Note that once the board resets, wifi will be disabled (see boot.py)
