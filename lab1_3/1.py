import math
#Функция для проверки введенных пользователем данных (проверка на символы)
def check_digit(num):
    #Если введенные данные являются числом, возвращается значение True
    if num.replace(".", "").replace("-", "").isdigit():
        return True
    #Если введенные данные не являются числом, возвращается значение False
    else:
        print("Вы ввели не число")
        return False

#Функция для проверки введенных пользователем данных (проверка на 0)
def check_zero(num):
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
def get_square(a, b, c):
    #Вычисление полупериметра
    perim = (a + b + c) / 2
    #Вычисление площади треугольника по формуле герона
    square = math.sqrt(perim * (perim - a) * (perim - b) * (perim - c))
    return round(square, 2)

#Функция для вычисления типа треугольника
def get_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

#Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на символы и на 0. Если обе проверки пройдены преобразовываем переменную из str в float
while True:
    side_1 = input("1 сторона: ")
    if check_digit(side_1) and check_zero(side_1):
        side_1 = float(side_1)
        break

#Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на символы и на 0. Если обе проверки пройдены преобразовываем переменную из str в float
while True:
    side_2 = input("2 сторона: ")
    if check_digit(side_2) and check_zero(side_2):
        side_2 = float(side_2)
        break

#Внутри цикла while с условием True вводим с клавиатуры значения стороны и устраиваем проверкку на символы и на 0. Если обе проверки пройдены преобразовываем переменную из str в float
while True:
    side_3 = input("3 сторона: ")
    if check_digit(side_3) and check_zero(side_3):
        side_3 = float(side_3)
        break
#С помощью конструкции if-else проверяем на то что сумма двух сторон больше третьей стороны
if side_1 + side_2 < side_3 or side_1 + side_3 < side_2 or side_2 + side_3 < side_1:
    print("Сумма двух сторон должна быть меньше третьей. Попробуйте еще раз")
#Если условие не выполняется (т.е. третья сторона < суммы двух других), вызываем 2 функции (площадь и тип)
else:
    print(f"Площадь треугольника: {get_square(side_1, side_2, side_3)}\nТип треугольника: {get_type(side_1, side_2, side_3)}")
