import math
#Функция для проверки введенных пользователем данных (проверка на 0)
def check_zero_3(num):
    #Преобразовываем параметр num из str в float
    num = float(num)
    #Если num > 0, возвращается True
    if num > 0:
        return True
    #Если num !> 0, возвращается False
    else:
        print("Сторона треугольника не может быть < или = 0")
        return False

#Функция для вычисления площади треугольника
def get_square_3(a, b, c):
    #Вычисление полупериметра
    perim = (a + b + c) / 2
    #Вычисление площади треугольника по формуле герона
    square = math.sqrt(perim * (perim - a) * (perim - b) * (perim - c))
    return round(square, 2)

#Функция для вычисления типа треугольника
def get_type_3(a, b, c):
    if c ** 2 == a ** 2 + b ** 2:
        return "Прямоугольный"
    elif c ** 2 < a ** 2 + b ** 2:
        return "Остроугольный"
    else:
        return "Тупоугольный"


# #Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на 0. Если проверка пройдена преобразовываем переменную из str в float
# while True:
#     side_1 = input("1 сторона: ")
#     if check_zero_3(side_1):
#         side_1 = float(side_1)
#         break
#
# #Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на 0. Если проверка пройдена преобразовываем переменную из str в float
# while True:
#     side_2 = input("2 сторона: ")
#     if check_zero_3(side_2):
#         side_2 = float(side_2)
#         break
#
# #Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на 0. Если проверка пройдена преобразовываем переменную из str в float
# while True:
#     side_3 = input("3 сторона: ")
#     if check_zero_3(side_3):
#         side_3 = float(side_3)
#         break
# #С помощью конструкции if-else проверяем на то что сумма двух сторон больше третьей стороны
# if side_1 + side_2 < side_3 or side_1 + side_3 < side_2 or side_2 + side_3 < side_1:
#     print("Сумма двух сторон должна быть меньше третьей. Попробуйте еще раз")
# #Если условие не выполняется (т.е. третья сторона < суммы двух других), вызываем 2 функции (площадь и тип)
# else:
#     print(f"Площадь треугольника: {get_square_3(side_1, side_2, side_3)}\nТип треугольника: {get_type_3(side_1, side_2, side_3)}")