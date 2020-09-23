# Jetson-nano-WS2812-LED-
This is the code for Jetson nano for producing WS2812 signal.

This is Python3 code.

## Preparation
### Configuring SPI in Jetson-IO tool
````
$ sudo /opt/nvidia/jetson-io/jetson-io.py
````

## Connection.
The signal pins are connected to 19 pins for spi1 or 13 pins for spi2.
Due to the spi communication protocol, the pins used for spi communication (21, 23, 24, and 26 for spi1) will be unavailable.
GND must also be connected.
Power must be supplied accordingly.

## Installing spidev by pip
````
$ sudo pip install spidev
````

## Usage.
````
SPItoWS(<number of LEDs>)
````
### LED designation.

````
SPItoWS.RGBto3Bytes(i, R, G, B)
````
i: Position of the LED
R, G, B: LED intensity, limited to 0-255

### LED glow.

````
SPItoWS.LED_show()
````
Use the RGBto3Bytes function to make the specified LEDs glow.

### Turn off all.
````
SPItoWS.LED_OFF_ALL()
````
Turn off all LEDs.
