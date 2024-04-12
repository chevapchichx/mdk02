# Создаем функцию с параметрами a и b, которая должна вернуть список простых чисел на отрезке от 'a' до 'b'
def primes(a, b):
    # Вводим пустой массив res, в котором будет храниться список простых чисел
    res = []

    # Создаем цикл for с итератором i и функцией range с параметрами a и b, который перебирает каждое число в диапазоне от a до b
    for i in range(a, b):

        # Вводим переменную c с исходным значением 0 (это будет счетчик)
        c = 0
        # Создаем цикл for с итератором j и функцией range с параметрами 1 и i, который перебирает каждое число в диапазоне от 1 до i
        for j in range(1, i):
            # С помощью оператора if с условием, что остаток от деления i на j+1 равен 0, находятся простые числа и в счетчик (с) записывается 1
            if i % (j+1) == 0:
                c += 1

#С помощью оператора if с условием, что c равно 1, находится число удовлетворяющее условию i % (j+1) == 0 (простое число) и число (i) добавляется в конец массива res
        if c == 1:
            res.append(i)
    # Функция sum_of_digits возвращает массив res, в котором хранится список простых чисел на отрезке от 'a' до 'b'
    return res

print(primes(0, 25))


# #Создаем функцию с параметрами a и b, которая по условию задачи должна вернуть список простых чисел на отрезке от 'a' до 'b'
# def primes(a, b):
#     #Вводим пустой массив res, в котором будет храниться список простых чисел
#     res = []
#     #Вводим переменную с со значением 0 (это будет счетчик)
#     #Однако здесь присутствует ошибка, из-за чего счетчик работает некорректно
#     c = 0
#     #Создаем цикл for с итератором i и функцией range с параметрами a и b, который перебирает каждое число в диапазоне от a до b
#     for i in range(a, b):
#         #Создаем цикл for с итератором j и функцией range с параметром i, который перебирает каждое число в диапазоне от 0 до i
#         #Однако здесь присутствует ошибка, из-за чего условие задачи не выполняется
#         for j in range(i):
#             #С помощью оператора if с условием, что остаток от деления i на j+1 равен 0, находятся простые числа и в счетчик (с) записывается 1
#             if i % (j + 1) == 0:
#                 c += 1
#             #С помощью оператора if с условием, что c равно 2, по условию задачи число (i) добавляется в конец массива res
#             #Однако здесь присутствует ошибка, из-за чего условие задачи не выполняется
#             if c == 2: #(ошибка - табуляция)
#                 res.append(i)
#     #Функция sum_of_digits возвращает массив res, в котором по условию задачи хранится список простых чисел на отрезке от 'a' до 'b'
#     return res
#
# #print(primes(0, 25))
















