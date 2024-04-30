import random

computer = random.randint(1,20)
turns = 0

while True:
    turns += 1
    user = int(input("Guess a number between 1 and 20: "))
    if user == computer:
        print(f"Good guess!")
        break
    elif user < computer:
        print(f"Your guess is too small, try again")
    else:
        print(f"Your guess is too big, try again")
print(f"Congradulations! you found the correct number after {turns} rounds")
