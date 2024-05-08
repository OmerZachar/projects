import random
rand_num = random.randint(1,20)

def play_game():
    counter = 0

    while True:
        user = input("Guess a number between 1 and 20 (x=Stop, n=restart, s=show answer): ")
        if user.isnumeric():
            userint = int(user)
            counter+=1
            if userint < rand_num:
                print('The number is too small, guess again')
            elif userint > rand_num:
                print('The number is too big, guess again')
            else:
                print(f"Congradulations! you answered correctly after {counter} times")
                return "success"

        else:
            if user.lower() == 'x':
                print("Game done!")
                return "exit"
            elif user.lower() == 's':
                print(f"The random number is {rand_num}")
                return "show"
            elif user.lower() == 'n':

                return "restart"
            else:
                print("type correctly!!!!!!")


def main():
    i=True
    while True:
        result = play_game()
        if result == 'exit':
            break
        elif result == "show":
            break
        elif result == 'restart':
            asking = input("would you like to play again (yes/no)?")
            if asking.lower() == 'yes':
                main()
            else:
                print("Good luck!")
                break
        elif result == "success":
            ask_user = input("would you like to play again (yes/no)?")
            if ask_user.lower() == 'no':
                print("Good luck!")
                break
            elif ask_user.lower() == 'yes':
                main()
            else:
                print("Please select yes/no")
                continue

main()
