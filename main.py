from symbolic_permission import symbolic_permission_value
from numeric_permission import numeric_permission_value
import os


def program_start():
    print("Would you like to get your permission in symbolic characters or numeric value?")
    print("Press 1 for symbolic\nPress 2 for numeric")
    user_selection = input()
    while user_selection != 1 or user_selection != 2:
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("Impossible, try again")
            user_selection = input()
            continue
        if user_selection < 0:
            print("Impossible, try again")
        if user_selection > 2:
            print("Impossible, try again")
        if user_selection == "1":
            print(symbolic_permission_value())
        else:
            print(numeric_permission_value())


program_start()

os.system("pause")
