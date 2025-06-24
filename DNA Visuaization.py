import random
import sys
import time
pause = 0.1
# DNA structuer
Rows = [
   '                       ##',
   '                      #{}-{}#',
   '                     #{}---{}#',
   '                    #{}----{}#',
   '                   #{}-----{}#',
   '                   #{}----{}#',
   '                   #{}---{}#',
   '                    #{}--{}#',
   '                     #{}-{}#',
   '                       ##',
   '                      #{}-{}#',
   '                     #{}---{}#',
   '                    #{}----{}#',
   '                   #{}-----{}#',
   '                   #{}----{}#',
   '                   #{}---{}#',
   '                    #{}--{}#',
   '                     #{}-{}#']

print('Press Ctrl-C to quit....')
time.sleep(2)
rowIndex = 0
# main program loop
while True:
    # Increment row 
    rowIndex += 1
    if rowIndex == len(Rows):
        rowIndex = 0

    if rowIndex == 0 or rowIndex == 9:
        print(Rows[rowIndex])
        continue
    # seclet random pair
    randomselection = random.randint(1 , 4)
    if randomselection == 1:
        leftnucleotide , rightnucleotide = 'A' , 'T'   
    elif randomselection == 2:
        leftnucleotide , rightnucleotide = 'T' , 'A'   
    elif randomselection == 3:
        leftnucleotide , rightnucleotide = 'C' , 'G'   
    elif randomselection == 4:
        leftnucleotide , rightnucleotide = 'G' , 'C'
    # print row 
    print(Rows[rowIndex].format(leftnucleotide,rightnucleotide))
    time.sleep(pause)


















