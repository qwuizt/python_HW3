from random import randint

amount_numbers = int(input("Введите размер списка: "))


def fill_list(size_list):
    my_list = []
    for _ in range (0, size_list):
        my_list.append(randint(0,9))
    return my_list
my_list = fill_list(amount_numbers)

def multiply_pairs(my_list):
    pair_list = []
    amount_pairs = len(my_list) // 2
    for i in range(0, amount_pairs):
        pair_list.append(my_list[i] * my_list[-1-i])
    if len(my_list) % 2 != 0:
        pair_list.append(my_list[amount_pairs])
    return pair_list 
print(my_list, "произведение пар ->", multiply_pairs(my_list))
