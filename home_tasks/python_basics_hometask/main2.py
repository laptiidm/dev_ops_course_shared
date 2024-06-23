import random

def create_user_list(attempt_quantity=5) -> list[int]:
    user_list = []
    print(f"Enter {attempt_quantity} different numbers from 1 to 100: ")

    for i in range(attempt_quantity):
        try:
            user_input = float(input(f"Enter {i + 1} number: "))
            user_list.append(int(user_input))
        except ValueError:
            print("Invalid input. Error.")
            print("You lost the attempt :((")
            continue
        print("ok, continue...")
    return user_list

def comparer(user_list: list[int], secret_list: list[int]) -> list[int]:
    matches = []
    for i in secret_list:
        for j in user_list:
            if i == j:
                matches.append(i)
    return matches


def new_game():
    user = input("ENTER YOUR NAME PLEASE: ")

    secret_list = [random.randint(1, 100) for _ in range(10)]
    user_list = create_user_list()
    mathes = comparer(user_list, secret_list)
    empty_or_not = len(mathes)

    print(f"The random nubers was: {secret_list}")
    print(f"Your entered numbers was: {user_list}")
    if empty_or_not > 0:
        print(f"{user}, Good job, you guessed next number(s): {mathes}")
    else:
        print("No matches found, {user}. Try again.")
    

new_game()
