n = int(input("Задайте число: "))
my_list =[1,0,1]
if n == 0:
    print(0)
else:
    negative_digit1, negative_digit2 = 0, 1
    for i in range (-2, -n-1, -1):
        negative_digit1, negative_digit2 = negative_digit2,  negative_digit1 - negative_digit2
        my_list = [negative_digit2] + my_list
    positive_digit1, positive_digit2 = 0, 1
    for i in range(2, n + 1):
        positive_digit1, positive_digit2 = positive_digit2, positive_digit1 + positive_digit2
        my_list.append(positive_digit2)
print("Списоок чисел Фибоначчи: ", my_list)