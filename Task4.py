# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
import random
os.system('cls')

n = int(input('Enter a number: '))

# Variant 1
print('Variant 1: binary format of', n, '=', format(n, 'b'))

# Variant2
def binary_format(number):
    binary_list = []
    remainder = 0
    while number > 0:
        remainder = number % 2
        binary_list.append(remainder)
        number = number//2

    print(f'Variant 2: binary format of {n} = ', *binary_list, sep='')

binary_format(n)