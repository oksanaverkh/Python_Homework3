# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

import os
os.system('cls')

num = int(input('Enter a number: '))

if num <= 0:
    print('Enter another value')

else:
    def nega_fibonacci(num):
        fib1, fib2 = -1, 1
        negative_fib_list = []
        for i in range(-num+1, 2):
            fib2, fib1 = (-1**(num+1))*(fib1 + fib2), (-1**(num+1))*fib2
            negative_fib_list.append(fib2)
        
        negative_fib_list.reverse()
        print(*negative_fib_list, sep=" ", end = ' ')
        return negative_fib_list

    def pos_fibonacci(num):
        fib1 = fib2 = 1
        print(fib1, fib2, end=' ')
        for i in range(2, num):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end=' ')
        return fib2

    nega_fibonacci(num)
    pos_fibonacci(num)