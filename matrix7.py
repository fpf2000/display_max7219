import max7219.led as led
from random import randint
import time
import os


matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

#def main():

 #       import os
temp = os.system ('/opt/vc/bin/vcgencmd measure_temp')

matrix.show_message(str(temp))
time.sleep(5)

t = (time.strftime("%d.%m.%Y %H:%M:%S"))

matrix.show_message(str(t))

time.sleep(2)

matrix.clear()
