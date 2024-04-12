#Вводим целочисленную переменную n с клавиатуры
n = int(input())
#Вводим переменную min_digit, которая равна 9
min_digit = 9
#Создаем цикл while с условием, что n > 0
while n > 0:
# Вводим переменную digit, в которую записывается остаток от деления n на 10
    digit = n % 10
#Используем конструкцию if для вычисления наименьшей цифры числа
#Если digit < min_digit
    if digit < min_digit:
#То значение записанное в digit присваивается в переменную min_digit
        digit = min_digit
#Записываем результат деления n на 10 без остатка
    n //= 10
#Выводим min_digit
print(min_digit)