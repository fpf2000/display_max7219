import max7219.led as led
from random import randint
import time
import os
import csv
import json

matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

prompt  = "\nINFO: "
prompt += "\nGebe 'quit' ein  zum Beenden !"

active = True
while active:
	message = (prompt)
	
	if message == 'quit':
             break
        else:
             temp = os.system ('/home/pi/E3dcGui/S10history/./S10history --brief |grep Day-CSV >daye3dc.csv')

             filename = '/home/pi/daye3dc.csv'
	     with open(filename) as f:
	      reader = csv.reader(f,delimiter=';')
	      header_row = next(reader)

#   for index, column_header in enumerate(header_row):
	      battin =[]
	      for row in reader:
	       battin.append(row[3])

	       print(row)

             t = (time.strftime("%H:%M Uhr"))

	     matrix.show_message(str(t))
	     time.sleep(1)
	     matrix.clear()


             matrix.show_message(str(row[3].title()) +" %"+" AKKU")
	     matrix.clear()
	     time.sleep(1)

	     matrix.clear()

	     solarinfo = row

	     filename = 'solarinfo.json'
	     with open(filename, 'w') as f_obj:
	        json.dump(solarinfo, f_obj)

	     time.sleep(60)
