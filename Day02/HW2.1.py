import random 
select = random.randint(1, 20)
user_input = int(input("Guess a number between 1 and 20: "))
counter = 1

while True:
    if user_input < select:
        print('The number is too small, guess again')
    elif user_input > select:
        print('The number is too big, guess again')
    else:
        break 

    counter += 1
    user_input = int(input("Guess a number between 1 and 20: "))

print(f"Congratulations! You answered correctly after {counter} times.")
