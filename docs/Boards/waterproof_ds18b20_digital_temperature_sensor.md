---
title: "Waterproof DS18B20 Digital Temperature Sensor"
sidebar_position: 215
tags:
    - "Sensor"
image: "/img/boards/waterproof_ds18b20_digital_temperature_sensor.png"
description: "Brand: Adafruit, Model: None"
---
# Waterproof DS18B20 Digital Temperature Sensor

![waterproof_ds18b20_digital_temperature_sensor](/img/boards/waterproof_ds18b20_digital_temperature_sensor.png)

## Basic information

**Brand**: Adafruit

**Product page**: [https://www.adafruit.com/product/381](https://www.adafruit.com/product/381)

**Documentation**: [https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf](https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf)

## Description

This is a pre\-wired and waterproofed version of the DS18B20 sensor\. Handy for when you need to measure something far away, or in wet conditions\. While the sensor is good up to 125°C the cable is jacketed in PVC so we suggest keeping it under 100°C\. Because they are digital, you don't get any signal degradation even over long distances\! These 1\-wire digital temperature sensors are fairly precise \(±0\.5°C over much of the range\) and can give up to 12 bits of precision from the onboard digital\-to\-analog converter\. They work great with any microcontroller using a single digital pin, and you can even connect multiple ones to the same pin, each one has a unique 64\-bit ID burned in at the factory to differentiate them\. Usable with 3\.0\-5\.0V systems\.



The only downside is they use the Dallas 1\-Wire protocol, which is somewhat complex, and requires a bunch of code to parse out the communication\. If you want something really simple, and you have an analog input pin, the TMP36 is trivial to get going\.



We toss in a 4\.7k resistor, which is required as a pullup from the DATA to VCC line when using the sensor\. We don't have a detailed tutorial up yet but you can get started by using the Dallas Temperature Control Arduino library which requires also the OneWire Library\.

