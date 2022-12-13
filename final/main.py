'''
    NUMBER GUESS: This is a numberbguessing game
'''
import random
state = True
print("I'm thinking of a number between 1 and 99")

computer_number = random.randint(1, 100)

while state:
    user_number = int(input("Enter a number: "))
    if user_number > computer_number:
        print('Your guess is too high')
    elif user_number < computer_number:
        print('Your guess is too low')
    else:
        print(f"Congrats! The number was {computer_number}")
        state = False
