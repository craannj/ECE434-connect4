# ECE 434 Final Project - Connect 4

## Overview
 This project involves using an 8x8 led matrix with the Beaglebone black to play Connect 4. The game is playable using rotary encoders and buttons on the breadboard. The code automatically does 4 in a row detection and will declare a winner

## Installation
Ssh into your Beaglebone and ensure it is connected to the internet.

Clone the following git repo with:
```
bone$ git clone https://github.com/craannj/ECE434-connect4.git
```
If the Adafruit Beaglebone IO Python Library is not already installed, install it with install.sh:
```
bone$ sudo install.sh
```
Or install it with these instructions:
```
bone$ sudo apt-get update
bone$ sudo apt-get install build-essential python3-dev python3-pip -y
bone$ sudo pip3 install Adafruit_BBIO
```
## Setup and Play

Once everything is installed you can run the pin configuration and then run the program.

Configure the pins:
```
bone$ ./pinconfig.sh
```
Run the program:
```
bone$  sudo ./connect4final.py
```
Note: The program has to be run using sudo to allow for I2C to function as intended.
