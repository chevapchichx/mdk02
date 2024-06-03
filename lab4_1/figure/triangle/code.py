import math  # импорт модуля math

__default_a, __default_b, __default_c = 7, 2, 8  # задаем значения по умолчанию для сторон треугольника


# создаем функцию, которая вычисляет и возвращает периметр треугольника
def triangle_perimeter(a=__default_a, b=__default_b, c=__default_c):
    return a + b + c


# создаем функцию, которая вычисляет и возвращает площадь треугольника по формуле Герона с округлением до 2 знаков
def triangle_area(a=__default_a, b=__default_b, c=__default_c):
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
