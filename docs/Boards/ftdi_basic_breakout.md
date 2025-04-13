---
title: "FTDI Basic Breakout"
sidebar_position: 83
tags:
    - "Circuit Boards"
image: "/img/boards/ftdi_basic_breakout.png"
description: "Brand: DFRobot, Model: None"
---
# FTDI Basic Breakout

![ftdi_basic_breakout](/img/boards/ftdi_basic_breakout.png)

## Basic information

**Brand**: DFRobot

**Product page**: [https://www.dfrobot.com/product-147.html](https://www.dfrobot.com/product-147.html)

**Documentation**: [http://image.dfrobot.com/image/data/DFR0065/DFR0065_sch...](http://image.dfrobot.com/image/data/DFR0065/DFR0065_schematics.pdf)

## Description

Introduction:



This is a basic breakout board for the FTDI FT232RL USB to serial IC\. The pinout of this board matches the FTDI cable to work with official Arduino and cloned 3\.3V Arduino boards\. It can also be used for general serial applications\. The major difference with this board is that it brings out the DTR pin as opposed to the RTS pin of the FTDI cable\. The DTR pin allows an Arduino target to auto\-reset when a new Sketch is downloaded\. This is a really nice feature to have and allows a sketch to be downloaded without having to hit the reset button\. This board will auto reset any Arduino board that has the reset pin brought out to a 6\-pin connector\.



The pins labeled BLK and GRN correspond to the colored wires on the FTDI cable\. The black wire on the FTDI cable is GND, green is DTR\. Use these BLK and GRN pins to align the FTDI basic board with your Arduino target\.



There are pros and cons to the FTDI Cable vs the FTDI Basic\. This board has TX and RX LEDs that allow you to actually see serial traffic on the LEDs to verify if the board is working, but this board requires a miniB cable\. The FTDI Cable is well protected against the elements, but is large and cannot be embedded into a project as easily\. The FTDI Basic uses DTR to cause a hardware reset where the FTDI cable uses the RTS signal\.



This board was designed to decrease the cost of Arduino development and increase ease of use \(the auto\-reset feature rocks\!\)\. Our Arduino Pro and LilyPad boards use this type of connector\.



Compatiblity



DFRduino Funnel I/O\(http://www\.dfrobot\.com/index\.php?route=product/product&path=35\_38&product\_id=111\) \(Fio\)

9 DOF IMU unit\(http://www\.dfrobot\.com/index\.php?route=product/product&keyword=9dof&category\_id=0&product\_id=187\)

Specifications:



3\.3/5V output\(switchable via Jumpers\)

