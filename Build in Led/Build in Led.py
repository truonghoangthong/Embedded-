from machine import Pin
from utime import sleep


print("LED starts flashing...")
led = Pin(16,Pin.OUT)
while True: 
    led.toggle()
    sleep(1) # sleep 1sec

