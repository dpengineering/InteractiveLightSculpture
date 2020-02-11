import board
import busio
import digitalio
import adfr
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
latch = digitalio.DigitalInOut(board.D14)
tlc5947 = adfr.TLC5947(spi, latch, num_drivers = 3)
count = 0

while(count < 64):
    tlc5947[count] = 2048
    count+=1
