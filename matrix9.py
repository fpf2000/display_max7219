import max7219.led as led
from random import randint
import time
import os


matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

#Text eingabe und Ausgabe 
w = raw_input("Text bitte: ")

matrix.show_message(str(w))

time.sleep(2)

matrix.clear()


# Anzeige des Datums und Uhrzeit ==> (time.strftime("%d.%m.%Y %H:%M:%S"))
t = (time.strftime("%H:%M"))

matrix.show_message(str(t))

time.sleep(2)

matrix.clear()

