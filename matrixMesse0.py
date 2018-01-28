import max7219.led as led
from random import randint
import time

matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

#deviceiD=1

matrix.show_message("Flucht Weg")
#matrix.clear()

i = 1
for i in range (1, 100): 
	matrix.show_message("Bytespeicher Erfurt ")
	matrix.show_message("X B X C V")
	time.sleep(1)
matrix.clear()

#n = int(input("Zahl bitte: "))

#for n in range (1, n):
#        matrix.show_message(str(n))
 #       time.sleep(1)

#matrix.clear()

#w = raw_input("Text bitte: ")

#matrix.show_message(str(w))

#time.sleep(5)

matrix.clear()
