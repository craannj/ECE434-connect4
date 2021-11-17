#!/usr/bin/env python3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import math

bus = smbus.SMBus(2)
bus2 = smbus.SMBus(1) 
matrix = 0x70
adxl = 0x53

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
winner = 0

screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
         
clear = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

rows, cols = (8, 8)
arr = [[0 for i in range(cols)] for j in range(rows)]
x_array = 0
y_array = 0

# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (p15)
bus.write_byte_data(matrix, 0xe7, 0)
# Writes initial matrix to the screen
bus.write_i2c_block_data(matrix, 0, screen)

bus2.write_byte_data(adxl, 0x2c, 0x08)
bus2.write_byte_data(adxl, 0x2d, 0x08)
bus2.write_byte_data(adxl, 0x31, 0x08)


def placeRedPiece(arr, xpos, xpos_old, ypos, ypos_old):
    places = 0
    GPIO.output(out, GPIO.LOW)
    total = screen[xpos] + screen[xpos-1] - 1
    xpos_old = screen[xpos] - 1
    if(total == 0):
        for i in range(7):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
    
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
    arr[int(math.log2(ypos))][int(math.ceil((xpos/2) - 1))] = 1
    return screen, ypos, arr
    
def placeGreenPiece(arr, xpos, xpos_old, ypos, ypos_old):
    places = 0
    total = screen[xpos] + screen[xpos+1] - 1
    xpos_old = screen[xpos] - 1
    GPIO.output(out, GPIO.LOW)
    if(total == 0):
        for i in range(7):
            ypos = ypos << 1
            screen[xpos] = 0x00
            screen[xpos] = screen[xpos] | ypos
            bus.write_i2c_block_data(matrix, 0, screen)
            ypos_old = ypos
            time.sleep(0.25)
    
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
    arr[int(math.log2(ypos))][int(math.ceil((xpos/2)))] = 2
    return screen, ypos, arr

def checkWinner(arr, player):
    winner = 0
    height = len(arr)
    width = len(arr[0])
    # check horizontal spaces
    for y in range(height):
        for x in range(width - 3):
            if arr[x][y] == player and arr[x+1][y] == player and arr[x+2][y] == player and arr[x+3][y] == player:
                return player

    # check vertical spaces
    for x in range(width):
        for y in range(height - 3):
            if arr[x][y] == player and arr[x][y+1] == player and arr[x][y+2] == player and arr[x][y+3] == player:
                return player

    # check / diagonal spaces
    for x in range(width - 3):
        for y in range(3, height):
            if arr[x][y] == player and arr[x+1][y-1] == player and arr[x+2][y-2] == player and arr[x+3][y-3] == player:
                return player

    # check \ diagonal spaces
    for x in range(width - 3):
        for y in range(height - 3):
            if arr[x][y] == player and arr[x+1][y+1] == player and arr[x+2][y+2] == player and arr[x+3][y+3] == player:
                return player    
    return winner

while True:
    accl3 = bus2.read_byte_data(adxl, 0x34)
    accl4 = bus2.read_byte_data(adxl, 0x35)
    
    accly = ((accl4&0x03)) + accl3    
    
    
    if(player == 1):
        GPIO.output(out, GPIO.HIGH)
        GPIO.output(out2, GPIO.LOW)
        if(horizontal.position < -4):
            if(xpos < 15):
                xpos = xpos + 2
        elif(horizontal.position > 4):
            if(xpos > 3):
                xpos = xpos - 2
        horizontal.position = 0
        
    #Update the matrix
        if(screen[xpos_old] > 0):
            screen[xpos_old] = screen[xpos_old] - 1
            bus.write_i2c_block_data(matrix, 0, screen)
        screen[xpos] = screen[xpos] | ypos
        bus.write_i2c_block_data(matrix, 0, screen)
        xpos_old = xpos
    
        if(GPIO.input(button1) == GPIO.HIGH and (screen[xpos] + screen[xpos-1]) < 253):
            screen, ypos, arr = placeRedPiece(arr, xpos, xpos_old, ypos, ypos_old)
            bus.write_i2c_block_data(matrix, 0, screen)
            xpos = 14
            xpos_old = 0
            ypos = 1
            winner = checkWinner(arr, player)
            player = 2
       
        if(accly < 200 and accly > 100):
            for i in range(16):
                screen[i] = 0x00
            bus.write_i2c_block_data(matrix, 0, screen)
            player = 1
            xpos = 15
            xpos_old = 0
            ypos = 1
            winner = 0
            
    elif(player == 2):
        GPIO.output(out, GPIO.LOW)
        GPIO.output(out2, GPIO.HIGH)
        if(horizontal.position < -4):
            if(xpos < 14):
                xpos = xpos + 2
        elif(horizontal.position > 4):
            if(xpos > 2):
                xpos = xpos - 2
        horizontal.position = 0        
        
        if(screen[xpos_old] > 0):
            screen[xpos_old] = screen[xpos_old] - 1
            bus.write_i2c_block_data(matrix, 0, screen)
        screen[xpos] = screen[xpos] | ypos
        bus.write_i2c_block_data(matrix, 0, screen)
        xpos_old = xpos        
        
        if(GPIO.input(button1) == GPIO.HIGH and (screen[xpos] + screen[xpos+1]) < 253):
            screen, ypos, arr = placeGreenPiece(arr, xpos, xpos_old, ypos, ypos_old)
            bus.write_i2c_block_data(matrix, 0, screen)            
            xpos = 15
            xpos_old = 0
            ypos = 1
            winner = checkWinner(arr, player)
            player = 1
            
        
        if(accly < 200 and accly > 100):
            for i in range(16):
                screen[i] = 0x00
            bus.write_i2c_block_data(matrix, 0, screen)
            xpos = 15
            xpos_old = 0
            ypos = 1
            player = 1
            winner = 0
       
            
    if(winner == 1):
        print("Red wins")
        for x in range(4):
            GPIO.output(out, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(out, GPIO.LOW)
            time.sleep(1)
           
        xpos = 14
        xpos_old = 0
        ypos = 1
        player = 2
        winner = 0
        for i in range(16):
            screen[i] = 0x00
            bus.write_i2c_block_data(matrix, 0, screen)
            time.sleep(0.25)
        arr = [[0 for i in range(cols)] for j in range(rows)]
    
    if(winner == 2):
        print("Green wins")
        for x in range(4):
            GPIO.output(out2, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(out2, GPIO.LOW)
            time.sleep(1)

        xpos = 15
        xpos_old = 0
        ypos = 1
        player = 1
        winner = 0
        for i in range(16):
            screen[i] = 0x00
            bus.write_i2c_block_data(matrix, 0, screen)
            time.sleep(0.25)
        arr = [[0 for i in range(cols)] for j in range(rows)]
    time.sleep(0.25)