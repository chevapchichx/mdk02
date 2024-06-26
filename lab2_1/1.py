# #Создаем функцию с параметром n, которая должна вернуть сумму цифр меньших 5 для положительного целого числа `n`. Если таких цифр нет, вернуть 0
# def sum_of_digits(n):
#     #Вводим переменную с со значением 0 (это будет счетчик)(ошибка - с написана кириллицей)
#     c = 0
#     #С помощью цикла while с условием, что n > 0, по условию задачи должна находиться сумма цифр меньших 5 для положительного целого числа `n`
#     #Однако в этом коде присутствует несколько ошибок, из-за чего условие задачи не выполняется
#     while n > 0:
#         #Вводим переменную digit, в которую записывается результат деления n на 10 без остатка
#         digit = n // 10
#         #С помощью оператора if с условием, что digit < 5, по условию задачи должны суммироваться цифры введенного числа (n) в переменной с, которые меньше 5
#         #Однако здесь присутствует ошибка, из-за чего условие задачи не выполняется
#         if digit < 5:
#             c = c + 1 #(ошибка - первая с написана кириллицей)
#         #Записываем в n результат деления n на 10 без остатка
#         n //= 10
#     #Функция sum_of_digits по условию задачи должна вернуть сумму цифр меньших 5 для положительного целого числа `n`, которая должна хранится в переменной с
#     #Однако эта функция вернет перeменную digit, в которой хранится результат деления n на 10 без остатка
#     return digit
#
# #print(sum_of_digits(int(input())))


# Создаем функцию с параметром n, которая по условию задачи должна вернуть сумму цифр меньших 5 для положительного целого числа `n`. Если таких цифр нет, вернуть 0
def sum_of_digits(n):
    # Вводим переменную c со значением 0 (это будет счетчик суммы цифр)
    c = 0
    # С помощью цикла while с условием, что n > 0, находится сумма цифр меньших 5 для положительного целого числа `n`

    while n > 0:
        # Вводим переменную digit, в которую записывается остаток от деления n на 10; она по очереди отсекает цифры с конца
        digit = n % 10
        # С помощью оператора if с условием, что digit < 5, суммируются цифры введенного числа (n) в переменной с, которые меньше 5

        if digit < 5:
            c = c + digit
        # Записываем в n результат деления n на 10 без остатка: уменьшаем n на 1 порядок
        n //= 10
    # Функция sum_of_digits возвращает сумму цифр меньших 5 для положительного целого числа `n`, которая хранится в переменной с
    # Если таких цифр нет функция вернет 0, т.к. с = 0
    return c

print(sum_of_digits(int(input())))


