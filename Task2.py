# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
import random
os.system('cls')

n = int(input('Enter list length: '))
limit = int(input('Enter list limit value: '))

if n <= 0 or limit <= 0:
    print('Enter another value')

else:
    def list_creation(n, limit):
        new_list = []
        for _ in range(n):
            new_list.append(random.randint(-limit, limit))
        return new_list

    def mult_pairs(new_list):
        prod_list = []
        mult_els = 0
        if n % 2 == 0:
            for i in range(len(new_list)//2):
                mult_els = new_list[len(new_list)-i-1] * new_list[i]
                prod_list.append(mult_els)
        else:
            for i in range(len(new_list)//2+1):
                if i != n//2+1:
                    mult_els = new_list[len(new_list)-i-1] * new_list[i]
                    prod_list.append(mult_els)
                else:
                    mult_els = new_list[n//2+1]** 2
                    prod_list.append(mult_els)
        return prod_list

    my_list = list_creation(n, limit)
    print(my_list)
    print(mult_pairs(my_list))
