from termcolor import colored
from Task_2 import find_negative_numbers

print(colored('Welcome to the Negative Number Finder!', 'green'))

while True:
    print('Please enter a list of integers separated by spaces (or type "exit" to quit):')
    user_input = input()
    if user_input.lower() == 'exit':
        break
    try:
        int_list = list(map(int, user_input.split()))
    except ValueError:
        print(colored('Invalid input! Please enter a list of integers separated by spaces.', 'red'))
        continue
    if len(int_list) == 1 and int_list[0] < 0:
        print(colored('The input list contains a negative number!', 'red'))
    else:
        result = find_negative_numbers(int_list)
        if result == 'True':
            print(colored('The input list contains a negative number!', 'red'))
        else:
            print(colored('The input list does not contain a negative number.', 'green'))