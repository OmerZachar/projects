import random
select = random.randint(1,20)
user = int(input("Guess a number between 1 and 20: "))
counter = 1
while user != select:
    if user < select:
        print('The number is too small, guess again')
    else:
        print('The number is too big, guess again')
    counter += 1  # Increment the counter after each guess
    user = int(input("Guess a number between 1 and 20: "))  # Get a new guess
    
print(f"Congradulations! you answered correctly after {counter} times")