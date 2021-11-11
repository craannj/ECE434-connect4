#!/usr/bin/env python3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import smbus
import time

bus = smbus.SMBus(2)
matrix = 0x70

#Left side encoder
horizontal = RotaryEncoder(eQEP2)
horizontal.setAbsolute()
horizontal.enable()

#Right side encoder
#vertical = RotaryEncoder(eQEP1)
#vertical.setAbsolute()
#vertical.enable()

#Start in top left corner of the matrix
xpos = 15   #Horizontal starting point
ypos= 1     #Vertical starting point

screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (p15)
bus.write_byte_data(matrix, 0xe7, 0)

bus.write_i2c_block_data(matrix, 0, screen)

while True:
    #Handle up and down
    #if(vertical.position > 0):
    #    if(ypos < 72):
    #        ypos = ypos << 1
    #elif(vertical.position < 0):
    #    if(ypos > 1):
    #        ypos = ypos >> 1
    #vertical.position = 0
    
    #Handle left and right
    if(horizontal.position < 0):
        if(xpos < 15):
            xpos = xpos + 2
    elif(horizontal.position > 0):
        if(xpos > 1):
            xpos = xpos - 2
    horizontal.position = 0

    #Update the matrix
    screen[xpos] = screen[xpos] | ypos
    bus.write_i2c_block_data(matrix, 0, screen)
    time.sleep(0.3)