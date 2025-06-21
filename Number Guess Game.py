import random

while True: #infinit loop
 
 # Welcome title
 print('Hi! Welcome to the number Guessing Game.\n You have 7 chances to guess the number.')
 print("Let's start")

 # Enter your higher and lower number
 low = int(input('Enter the Lower Bound: '))
 high = int(input('Enter the Upper Bound: '))
 print(f'You have 7 chances to guess the number between {low} and {high}')
 num = random.randint(low,high)

 total_chances = 7  # Total attempt
 guess_number = 0   # Your guess number

 # count your attempt
 while total_chances > guess_number:
    guess_number += 1
    guess = int(input('Enter your guess: '))

    # conditions
    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {guess_number} attempts.')
        print('Thanks For Playing This Game')
        break
    elif guess_number >= total_chances and num != guess:
        print(f'The number was {num}. Better luck next time.')
    elif guess > num:
        print('Too high! Try a lower number.')
    elif guess < num:
        print('Too low! Try a higher number')

    # using while loop to play game again
        print('Would you like to play this game again Yes/No')
 agian = input("Yes/No: ")
 if agian.startswith('y'):
    continue
 elif agian.startswith('n'):
    print('Thank You')
    break