# Jetson-nano-WS2812-LED-
This is the code for Jetson nano for producing WS2812 signal.

This is Python3 code.

## import
You have to import spidev.

You can install it via pip.

## How to use
SPItoWS class generates WS2812 signal via SPI connection.

Connect your SPI MOSI pin to LED tape's signal pin.

The GND connection is also needed.

It is recommended that power is not supplied from the Jetson nano.

## Code
SPItoWS(<The number of your LEDs>)
  SPItoWS.RGBto3Bytes(i, R, G, B)
  
i: The location of the LED.

R, G, B: The intensity of the LEDs. The number is limited to 0-255.
