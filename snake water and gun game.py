import random
# Loop
while True:
 number = [1,2,3]
 ran = random.choice(number)
 # 1 = Snake
 # 2 = Gun
 # 3 = Water
 print('1 Snake: 2 Gun: 3 Water')
 a = int(input(' Enter your choice '))
 if(a>=4):
    print('Type Invalied Number ') 
 # Conditions
 elif(a==ran):
    print('Game Draw')
 elif((ran==1 and a==3) or (ran==2 and a==1) or (ran==3 and a==2)):
    print('You Loser')
 else:
    print('You Win')
 # Play again yes or no   
 print('Play again (y) Yes or (n) No')
 again = input('Enter y/n:> ') 
 if again.startswith('y'):
   continue
 elif again.startswith('n'):
    print('Thank You For Play Game:')
    break