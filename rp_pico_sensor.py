import machine
import time
import utime
import sys


TRIG = machine.Pin(17,machine.Pin.OUT)
ECHO = machine.Pin(16,machine.Pin.IN)
buzz = machine.Pin(15, machine.Pin.OUT)
onled = machine.Pin(25, machine.Pin.OUT)
motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)



def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while not ECHO.value():
        pass
    time1 = time.ticks_us()
    while ECHO.value():
        pass
    time2 = time.ticks_us()
    during = time.ticks_diff(time2,time1)
    return during * 340 / 2 / 10000

while True:
    s = "" # Initialize s to 0 before the loop starts
    dis = distance()
    print(dis)
    time.sleep_ms(300)
    if dis < 43: 
        print("Flushing....")
        motor1A.high()
        motor2A.low()
        utime.sleep(0.5)
        print("Done")
        buzz.value(1)
        onled.value(1)
        utime.sleep(0.3)
        onled.value(0)
        buzz.value(0)
        utime.sleep(1)

