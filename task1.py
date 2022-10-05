from random import  randint


amount_numbers = int(input("Введите размер списка: "))

def fill_list(size_list):
    my_list = []
    for _ in range (0, size_list):
        my_list.append(randint(0,9))
    return my_list
my_list = fill_list(amount_numbers)

def calculate_sum (my_list):
    suma = 0
    for e in range(0, len(my_list)):
        if e % 2 == 0:
            suma += my_list[e]     
    return suma

print(my_list, "сумма -> ", calculate_sum(my_list))