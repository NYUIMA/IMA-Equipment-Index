---
title: "Bluetooth 2.0 (hc-05 gomcu)"
sidebar_position: 36
tags:
    - "Sensor"
image: "/img/boards/bluetooth_2.0_-hc-05_gomcu-.png"
description: "Brand: DSD Tech, Model: HC-05 gomcu"
---
# Bluetooth 2.0 (hc-05 gomcu)

![bluetooth_2.0_-hc-05_gomcu-](/img/boards/bluetooth_2.0_-hc-05_gomcu-.png)

## Basic information

**Brand**: DSD Tech

**Model**: HC-05 gomcu

**Product page**: [https://www.amazon.com/DSD-TECH-HC-05-Bluetooth-Wireles...](https://www.amazon.com/DSD-TECH-HC-05-Bluetooth-Wireless/dp/B074GMQ6G3)

**Documentation**: [https://www.gme.cz/data/attachments/dsh.772-148.1.pdf](https://www.gme.cz/data/attachments/dsh.772-148.1.pdf)

## Description

 

Your Arduino connected with this module is able to establish a wireless bluetooth connection with your pc or smartphone with built in bluetooth\.

 

This connection shall enable you send instructions from your pc or smartphone to your Arduino to control the Arduino, and enables you to send data from your Arduino to your pc or smartphone by wireless transmission\.

 

This HC\-05 Module is working at 3\.3V, but it is fitted on a baseboard that provide voltage regulation for you to input Arduino 5V to Vcc pin of this module\.

 

More details:\-

1\. Module size : 38\.5mm X 18\.5mm\.

2\. Able to be set as a Master or as a Slave via AT commands\.

3\. Use the CSR mainstream bluetooth chip, bluetooth V2\.0 protocol standards\.

4\. Onboard 3\.3V regulator chip\. Input to Vcc 5V and onboard regulator can regulate it to 3\.3V for internal module functioning\.

5\. Default baud rate of 9600, the user can change speed via AT commands\.

6\. Working current: not sure, i did not verified\.

7\. Provide 6 pin labeled as VCC, GND,TXD,RXD,KEY and LED\.

8\. Interface level is 3\.3V for the TXD and RXD of this module, in fact also advised to use 3\.3V logic for the KEY\. I had verified KEY working well on 3\.3V logic\.

9\. For 5V Arduino please use level shifter to shift from 5V TXD of Arduino to 3\.3V RXD of this module\. But you can direct connect 3\.3V TXD of this module to RXD of Arduino because Arduino side can interpret the incoming 3\.3V signal\.

10\. This module has the KEY pin, it is used for AT Command programming, please google“HC\-05 AT Command” to find out more information from internet\. I had verified and successfuly issue AT Command using the KEY pin at 3\.3V logic level\.

11\. LED pin of this module is meant for driving a external LED for status indication purpose\. LED pin defaults to high when bluetooth connected, and low when bluetooth disconnected\. However you can reprogram it to the reverse way via AT commands\. Some user reprogram it to reverse so that when bluetooth connected it is low and use it to act as DTR pin to reset Arduino for remote Arduino programming\.

12\. This module has no EN pin as in some other bluetooth module\.

13\. Open area transmission distance is not sure, i only verified the bluetooth connection is working with my tablet \(with bluetooth\) about 2 feet away from this module\. But i think it should be similar to other bluetooth modules that use the same chipset which is said to work within 10 feet in open air\. Figure is only for guidance only and actual working distance could be less\.

14\. After pairing provides a full duplex serial port that support 8 data bits and 1 stop bits and no parity, this is the most common communication format\.

15\. AT command reference manual will be send separately to buyer\.

16\. No schematics of the baseplate can be provided\.

