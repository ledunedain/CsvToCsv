import csv
import re
from unicodedata import normalize
from unittest import result
results = []
a,b = 'áAéÉíÍóÓúÚü','aaeeiioouuu'

trans = str.maketrans(a,b)

with open('Libro1.csv', encoding="utf-8") as File:
    reader = csv.reader(File, delimiter=';', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        results.append(row)

for i in results:
     for i2 in range(len(i)):
          i[i2] = i[i2].translate(trans)

myFile = open('example2.csv', 'w' , newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(results)
     
print("Writing complete")
