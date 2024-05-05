import random

computer = random.randint(1,20)
turns = 0

while True:
    turns += 1
    user = int(input("Guess a number between 1 and 20: "))
    if user == 'x':
        print('Game over')
        break
    elif user == 'n':
        print('Game over, Do u want to restart?')
        break
    elif user == 's':
        print(f"The number was {computer}")
        break
    else: 
        if user == computer:
            print(f"Good guess!")
            break
        elif user < computer:
            print(f"Your guess is too small, try again")
        else:
            print(f"Your guess is too big, try again")
            print(f"You found the correct number after {turns} rounds")