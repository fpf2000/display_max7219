import max7219.led as led
from random import randint
import time
import os
import csv


matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

#def main():

 #       import os
# csv Datei aus E3DChistory erzeugen und abspeichern
temp = os.system ('/home/pi/E3dcGui/S10history/./S10history --brief |grep Day-CSV >daye3dc.csv')

filename = '/home/pi/daye3dc.csv'
with open(filename) as f:
   reader = csv.reader(f,delimiter=';')
   header_row = next(reader)

#   for index, column_header in enumerate(header_row):
   battin =[]
   for row in reader:
       battin.append(row[1])


matrix.show_message(str(battin))
time.sleep(5)

t = (time.strftime("%d.%m.%Y %H:%M:%S"))

matrix.show_message(str(t))

time.sleep(2)

matrix.clear()
