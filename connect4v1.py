#!/usr/bin/env python3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)
matrix = 0x70

out = "P9_11"
out2 = "P9_13"
button1 = "P9_42"

GPIO.setup(out, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#Encoder
horizontal = RotaryEncoder(eQEP1)
horizontal.setAbsolute()
horizontal.enable()

#Start in top left corner of the matrix
xpos = 15   #Horizontal starting point
ypos = 1     #Vertical starting point
xpos_old = 15
ypos_old = 1

player = 1  # 1=red  2=green

screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
         
clear = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (p15)
bus.write_byte_data(matrix, 0xe7, 0)

bus.write_i2c_block_data(matrix, 0, screen)


def placeRedPiece(xpos, xpos_old, ypos, ypos_old):
    places = 0
    GPIO.output(out, GPIO.LOW)
    total = screen[xpos] + screen[xpos-1] - 1
    xpos_old = screen[xpos] - 1
    print(total)
    if(total == 0):
        for i in range(7):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        #screen[xpos] = screen[xpos] + 128
        #bus.write_i2c_block_data(matrix, 0, screen)
    
    elif(total == 128):
        for i in range(6):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 64
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 192):
        for i in range(5):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 32
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 224):
        for i in range(4):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 16
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 240):
        for i in range(3):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 8
        bus.write_i2c_block_data(matrix, 0, screen)

    elif(total == 248):
        for i in range(2):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 4
        bus.write_i2c_block_data(matrix, 0, screen)
    print(screen)
    return screen, ypos
    
def placeGreenPiece(xpos, xpos_old, ypos, ypos_old):
    places = 0
    total = screen[xpos] + screen[xpos+1] - 1
    xpos_old = screen[xpos] - 1
    print(total)
    GPIO.output(out, GPIO.LOW)
    if(total == 0):
        for i in range(7):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        #screen[xpos] = screen[xpos] + 128
        #bus.write_i2c_block_data(matrix, 0, screen)
    
    elif(total == 128):
        for i in range(6):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 64
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 192):
        for i in range(5):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 32
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 224):
        for i in range(4):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 16
        bus.write_i2c_block_data(matrix, 0, screen)
        
    elif(total == 240):
        for i in range(3):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 8
        bus.write_i2c_block_data(matrix, 0, screen)

    elif(total == 248):
        for i in range(2):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
        screen[xpos] = xpos_old + 4
        bus.write_i2c_block_data(matrix, 0, screen)
    print(screen)
    return screen, ypos


while True:
    if(player == 1):
        GPIO.output(out, GPIO.HIGH)
        GPIO.output(out2, GPIO.LOW)
        if(horizontal.position < 0):
            if(xpos < 15):
                xpos = xpos + 2
        elif(horizontal.position > 0):
            if(xpos > 1):
                xpos = xpos - 2
        horizontal.position = 0

    #Update the matrix
        if(screen[xpos_old] > 0):
            screen[xpos_old] = screen[xpos_old] - 1
            bus.write_i2c_block_data(matrix, 0, screen)
        screen[xpos] = screen[xpos] | ypos
        bus.write_i2c_block_data(matrix, 0, screen)
        xpos_old = xpos
    
        if(GPIO.input(button1) == GPIO.HIGH and screen[xpos] < 253):
            screen, ypos = placeRedPiece(xpos, xpos_old, ypos, ypos_old)
            bus.write_i2c_block_data(matrix, 0, screen)
            xpos = 14
            xpos_old = 0
            ypos = 1
            player = 2
            #print(screen)
            
    elif(player == 2):
        GPIO.output(out, GPIO.LOW)
        GPIO.output(out2, GPIO.HIGH)
        if(horizontal.position < 0):
            if(xpos < 14):
                xpos = xpos + 2
        elif(horizontal.position > 0):
            if(xpos > 1):
                xpos = xpos - 2
        horizontal.position = 0        
        
        if(screen[xpos_old] > 0):
            screen[xpos_old] = screen[xpos_old] - 1
            bus.write_i2c_block_data(matrix, 0, screen)
        screen[xpos] = screen[xpos] | ypos
        bus.write_i2c_block_data(matrix, 0, screen)
        xpos_old = xpos        
        
        if(GPIO.input(button1) == GPIO.HIGH and screen[xpos] < 253):
            screen, ypos = placeGreenPiece(xpos, xpos_old, ypos, ypos_old)
            bus.write_i2c_block_data(matrix, 0, screen)            
            xpos = 15
            xpos_old = 0
            ypos = 1
            player = 1
    #print(screen)
    time.sleep(0.25)
    