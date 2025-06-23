import sys
import time
import sevseg

# Enter Time in seconds
secondsLeft = int(input('Enter Your Timer: '))

# Main program loop
while True:
    # Get the hours/minutes/seconds
    hours = (secondsLeft // 3600)
    minutes = ((secondsLeft // 3600) % 60)
    second = (secondsLeft % 60)

    hDigits = sevseg.getSevSegStr(hours,2)
    hTopRow , hMiddleRow , hBottomRow = hDigits.splitlines()

    
    mDigits = sevseg.getSevSegStr(minutes,2)
    mTopRow , mMiddleRow , mBottomRow = mDigits.splitlines()

    sDigits = sevseg.getSevSegStr(second,2)
    sTopRow , sMiddleRow , sBottomRow = sDigits.splitlines()
    # Setup Display digits
    print('< Hours >      < Minutes >      < Seconds >')
    print(hTopRow     + '       ' + mTopRow     + '       ' + sTopRow)
    print(hMiddleRow  + '   *   ' + mMiddleRow  + '   *   ' + sMiddleRow)
    print(hBottomRow  + '   *   ' + mBottomRow  + '   *   ' + sBottomRow)

    if secondsLeft == 0:
        print()
        print('     * * * * BOOM * * * *')
        break

    print()
    print('Press Ctrl-C to quit.')

    time.sleep(1)
    secondsLeft -= 1

