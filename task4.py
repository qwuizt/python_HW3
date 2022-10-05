from random import uniform





amount_numbers = int(input("Введите размер списка: "))

def fill_list(size_list):
    my_list = []
    for _ in range (0, size_list):
        my_list.append(round(uniform(0,10),2))
    return my_list
my_list = fill_list(amount_numbers)

def find_min_max_fraction(my_list):
    new_list = []
    for i in range(0, len(my_list)):
        num_fract = my_list[i] % 1 
        new_list.append(round(num_fract,2))
    return max(new_list), min(new_list)

max_fract, min_fract = find_min_max_fraction(my_list)
difference = max_fract - min_fract


print(my_list, "MAX:", max_fract, "MIN:", min_fract, "Difference:", difference)

