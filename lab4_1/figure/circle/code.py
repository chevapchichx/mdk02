import math  # импорт модуля math

__default_radius = 5  # задаем значение по умолчанию для радиуса


# создаем функцию, которая вычисляет и возвращает длину окружности с округлением до 2 знаков после запятой
def circle_perimeter(radius=__default_radius):
    return round(2 * math.pi * radius, 2)


# создаем функцию, которая вычисляет и возвращает площадь окружности с округлением до 2 знаков после запятой
def circle_area(radius=__default_radius):
    return round(math.pi * radius ** 2, 2)

