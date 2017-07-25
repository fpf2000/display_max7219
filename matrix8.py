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
while True:
	import subprocess
	temp = subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1]
#	temp = subprocess.Popen(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)

#	temp = os.system ('/opt/vc/bin/vcgencmd measure_temp')

	matrix.show_message(str(temp))
	time.sleep(1)
	matrix.clear()
# Anzeige des Datums und Uhrzeit ==> (time.strftime("%d.%m.%Y %H:%M:%S"))

	t = (time.strftime("%H:%M"))

	matrix.show_message(str(t))

	time.sleep(2)

	matrix.clear()

	time.sleep(20)
