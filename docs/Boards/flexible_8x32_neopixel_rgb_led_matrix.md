---
title: "Flexible 8x32 NeoPixel RGB LED Matrix"
sidebar_position: 93
tags:
    - "Sensor"
image: "/img/boards/flexible_8x32_neopixel_rgb_led_matrix.png"
description: "Brand: Adafruit, Model: None"
---
# Flexible 8x32 NeoPixel RGB LED Matrix

![flexible_8x32_neopixel_rgb_led_matrix](/img/boards/flexible_8x32_neopixel_rgb_led_matrix.png)

## Basic information

**Brand**: Adafruit

**Product page**: [https://www.adafruit.com/product/2294](https://www.adafruit.com/product/2294)

**Documentation**: [https://learn.adafruit.com/adafruit-neopixel-uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide)

## Description

DESCRIPTION

For advanced NeoPixel fans, we how have a bendable, flexible 8x32 NeoPixel LED Matrix\! Control all 256 ultra\-bright LEDs using a single microcontroller pin, set each LED as you wish to scroll messages or draw little images\. This matrix has a thick flexible PCB backing that can be gently bent and curved around surfaces



You can use this matrix just like any other NeoPixel\-compatible product, and we even have NeoMatrix code that will let you use the matrix as a 8x32 grid for drawing on without having to do all the icky math Just initalize NeoMatrix with



Adafruit\_NeoMatrix matrix = Adafruit\_NeoMatrix\(32, 8, PIN,  NEO\_MATRIX\_TOP \+ NEO\_MATRIX\_LEFT \+ NEO\_MATRIX\_COLUMNS \+ NEO\_MATRIX\_ZIGZAG, NEO\_GRB \+ NEO\_KHZ800\);

Don't forget, with 256 LEDs, you could use over 15A of current if you turn on all the LEDs on to white \(which we really do not recommend because we don't think the flex PCB can handle that much current\)\. Try to keep the current draw at undrer 5A, you can use our 5V 4A or 5V 10A power supply\. For portable use, if you are drawing less than 3A, try out this 5V@3A UBEC\.



Please note: Flexible PCBs are not designed for repeated flexing\! While we think this product may work in wearables or other situations where the matrix is bent around, we do not offer any guarantees or refunds if you end up cracking the LEDs or traces\! This is for advanced users only, who already know how to use NeoPixels and are comfortable with the high current requirements and protecting the matrix from damage\. There are no returns, refunds or replacements for damaged product\. You cannot cut these panels into custom shapes as data/power lines run through the entire body of the PCB\.

