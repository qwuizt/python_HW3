
n = int(input("Введите десятичное число: "))
digit = ''
while n > 0:
    digit = str(n % 2) + digit
    n = n // 2
print(digit)
