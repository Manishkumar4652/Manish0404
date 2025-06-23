import time
import sys
import shutil
import random

min_strram_length = 100
max_strram_length = 100

pause = 0.2
stream_chars = ['0','1']

density = 0.02

width = shutil.get_terminal_size()[0]

width -= 1
print('Press Ctrl-C to quit')

time.sleep(2)

columns = [0] * width
while True:
    for i in range(width):
        if columns[i] == 0:
            if random.random() <= density:
                columns[i] = random.randint(min_strram_length,max_strram_length)
                
        if columns[i] > 0:
            print(random.choice(stream_chars),end='')
            columns[i] -= 1
        else:
            print('  ',end='')
    print()
    sys.stdout.flush()
    time.sleep(0.2)
