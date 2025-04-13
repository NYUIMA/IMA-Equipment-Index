---
title: "Bluetooth 2.0 (hc-05)"
sidebar_position: 37
tags:
    - "Sensor"
image: "/img/boards/bluetooth_2.0_-hc-05-.png"
description: "Brand: DSD TECH, Model: ZG-B28090W"
---
# Bluetooth 2.0 (hc-05)

![bluetooth_2.0_-hc-05-](/img/boards/bluetooth_2.0_-hc-05-.png)

## Basic information

**Brand**: DSD TECH

**Model**: ZG-B28090W

**Product page**: [https://www.amazon.com/DSD-TECH-HC-05-Bluetooth-Wireles...](https://www.amazon.com/DSD-TECH-HC-05-Bluetooth-Wireless/dp/B074GMQ6G3)

**Documentation**: [http://www.martyncurrey.com/arduino-with-hc-05-bluetoot...](http://www.martyncurrey.com/arduino-with-hc-05-bluetooth-module-at-mode/)

## Description

HC\-05



Master and slave mode can be switched



Master role: have no function to remember the last paired salve device\. It can be made paired to any slave device\. In other words, just set AT\+CMODE=1 when out of factory\. If you want HC\-05 to remember the last paired slave device address like HC\-06, you can set AT\+CMODE=0 after paired with the



Pairing: The master device can not only make pair with the specified Bluetooth address, like cell\-phone, computer adapter, slave device, but also can search and make pair with the slave device automatically\. Typical method: On some specific conditions, master device and slave device can make pair with each other automatically\. \(This is the default method\.\) other device\. Please refer the command set of HC\-05 for the details\.



Multi\-device communication: There is only point to point communication for modules, but the adapter can communicate with multi\-modules\.



AT Mode 1: After power on, it can enter the AT mode by triggering PIN34 with high level\. Then the baud rate for setting AT command is equal to the baud rate in communication, for example: 9600\. AT mode 2: First set the PIN34 as high level, or while on powering the module set the PIN34 to be high level, the Baud rate used here is 38400 bps\. Notice: All AT commands can be operated only when the PIN34 is at high level\. Only part of the AT commands can be used if PIN34 doesn’t keep the high level after entering to the AT mode\. Through this kind of designing, set permissions for the module is left to the user’s external control circuit, that makes the application of HC\-05 is very flexible\.



During the process of communication, the module can enter to AT mode by setting PIN34 to be high level\. By releasing PIN34, the module can go back to communication mode in which user can inquire some information dynamically\. For example, to inquire the pairing is finished or not\.



Default communication baud rate: 9600, 4800\-1\.3M are settable\.



KEY: PIN34, for entering to the AT mode\.



LED1: PIN31, indicator of Bluetooth mode\. Slow flicker \(1Hz\) represents entering to the AT mode2, while fast flicker\(2Hz\) represents entering to the AT mode1 or during the communication pairing\. Double flicker per second represents pairing is finished, the module is communicable\. LED2: PIN32, before pairing is at low level, after the pairing is at high level\. The using method of master and slaver’s indicator is the same\. Notice: The PIN of LED1 and LED2 are connected with LED\+\.



Consumption: During the pairing, the current is fluctuant in the range of 30\-40mA\. The mean current is about 25mA\. After paring, no matter processing communication or not, the current is 8mA\. There is no sleep mode\. This parameter is same for all the Bluetooth modules\.



Reset: PIN11, active if it’s input low level\. It can be suspended in using\.



Level: Civil

