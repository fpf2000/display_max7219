import max7219.led as led
from random import randint
import time

matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

# matrix.brightness(0)

# matrix.orientation(90)

#deviceiD=1

#matrix.show_message("Display Ausgaben")

#matrix.clear()

#i = 1
#for i in range (1, 2): 
#	matrix.show_message(str(i))
#	time.sleep(1)
#matrix.clear()

#n = int(input("Zahl bitte: "))

#for n in range (1, n):
#        matrix.show_message(str(n))
 #       time.sleep(1)

#matrix.clear()

# w = raw_input("Text bitte: ")

# w = "Es folgt Datum / Uhrzeit"

# matrix.show_message(str(w))

# time.sleep(5)

# t = (time.strftime("%d.%m.%Y %H:%M:%S"))

# matrix.show_message(str(t))

# time.sleep(2)

matrix.clear()

time .sleep(2)

matrix.clear()
