import csv
filename = '/home/pi/daye3dc.csv'
with open(filename) as f:
   reader = csv.reader(f,delimiter=';')
   header_row = next(reader)

#   for index, column_header in enumerate(header_row):
   battin =[]
   for row in reader:
       battin.append(row[1])

#   print(battin)
#       print(index,column_header)
