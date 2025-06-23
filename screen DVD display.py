import sys,random,time
# try:
import bext
# except ImportError:
#     sys.exit

width,height = bext.size()
width -= 1
number_of_logos = 5
pause_amount = 0.2
COLOR_KEY = ['red','green','yellow','blue','white']

up_right = 'ur'
up_left = 'ul'
down_right = 'dr'
down_left = 'dl'
DIRECTION = (up_right,up_left,down_right,down_left)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()
    logos = []
    for i in range(number_of_logos):
        logos.append({COLOR:random.choice(COLOR_KEY),X:random.randint(1,width-4)
                      ,Y:random.randint(1,height-4),DIR:random.choice(DIRECTION)})
        
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X],logo[Y])
            print(' ',end='')
            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == height - 1:
                logo[DIR] = up_right
                cornerBounces +=1
            elif logo[X] == width - 3 and logo[Y] == 0:
                logo[DIR] = down_left
                cornerBounces += 1
            elif logo[X] == width - 3 and logo[Y] == height - 1:
                logo[DIR] = up_left
                cornerBounces += 1
            elif logo[X] == 0 and logo[DIR] == up_left:
                logo[DIR] = up_right 
            elif logo[X] == 0 and logo[DIR] == down_left:
                logo[DIR] = down_right
            elif logo[X] == width - 3 and logo[DIR] == up_right:
                logo[DIR] = up_left
            elif logo[X] == width - 3 and logo[DIR] == down_right:
                logo[DIR] = down_left
            elif logo[Y] == 0 and logo[DIR] == up_left:
                logo[DIR] = down_left
            elif logo[Y] == 0 and logo[DIR] == up_right:
                logo[DIR] = down_right
            elif logo[Y] == height - 1 and logo[DIR] == down_left:
                logo[DIR] = up_left
            elif logo[Y] == height - 1 and logo[DIR] == down_right:
                logo[DIR] = up_right
            if logo[DIR] != originalDirection:
                    logo[COLOR] = random.choice(COLOR_KEY)
        for logo in logos:    
            if logo[DIR] == up_right:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == up_left:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == down_right:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == down_right:
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5,0)
        bext.fg('white')
        print('Corner bounces:',cornerBounces,end='')
        
        for logo in logos:
            bext.goto(logo[X],logo[Y])
            bext.fg(logo[COLOR])
            print('DVD',end='')
        bext.goto(0,0)
        sys.stdout.flush()
        time.sleep(pause_amount)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo , by AI Sweigart')
        sys.exit()            