import random
import os
import sys
sys.path.append(os.path.abspath('D:\QOSF_Tasks_8\Task_2.py'))
from Task_2 import find_negative_numbers

def generate_random_input_list(size):
    return [random.randint(-100, 100) for _ in range(size)]

def calculate_error_rate(num_tests, max_size):
    num_errors = 0
    for i in range(num_tests):
        size = random.randint(1, max_size)
        int_list = generate_random_input_list(size)
        expected_output = 'True' if any(x < 0 for x in int_list) else 'False'
        actual_output = find_negative_numbers(int_list)
        if actual_output != expected_output:
            num_errors += 1
    return num_errors / num_tests

error_rate = calculate_error_rate(num_tests=1000, max_size=10)
print(f'The error rate of the find_negative_numbers function is {error_rate:.2%}.')