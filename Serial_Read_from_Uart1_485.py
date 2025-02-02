from machine import UART, Pin
import time
BRate=1200
print("Baud Rate:" ,BRate)
# tx pin 0, rx pin 1
myUsart0 = UART(0, baudrate=BRate, bits=8, tx=Pin(0), rx=Pin(1), timeout=10)
# tx pin 4, rx pin 5
myUsart1 = UART(1, baudrate=BRate, bits=8, tx=Pin(4), rx=Pin(5), timeout=10)
try:
    while True:
        rxData = bytes() 
        time.sleep(0.1)
        while myUsart1.any() > 0:
        # while True:
            rxData += myUsart1.read(1)
            # print("any:",str(myUsart1.any()))
            # time.sleep(1)
        print("myUsart0: " , rxData.decode('utf-8'))
        
    
except KeyboardInterrupt:
    print("Keyboard")
    pass # machine.soft_reset()

   