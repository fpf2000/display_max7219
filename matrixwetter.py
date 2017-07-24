import max7219.led as led
from random import randint
import time
import os
from xml.dom.minidom import *
import urllib

matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)




#while True:
#Baum = parseString(Baum)
URL = "http://wetter.ringelberger.de/RSS/weewx_rss.xml"
Baum = urllib.urlopen(URL).read()
# Temperatur einlesen
#Temperatur = float(Today.attributes["temp"].value)
temp = Baum.getElementsByTagName('Outside temperature:')[0]
#temp = Temp.attributes["Outside temperature:"].value
print temp

#	import subprocess
#	temp = subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1]
#	temp = subprocess.Popen(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)

#	temp = os.system ('/opt/vc/bin/vcgencmd measure_temp')

#	matrix.show_message(str(temp))
#	time.sleep(5)
#	matrix.clear()


#	t = (time.strftime("%d.%m.%Y %H:%M:%S"))
#
#	matrix.show_message(str(t))

#	time.sleep(2)

#	matrix.clear()

#	time.sleep(2)
