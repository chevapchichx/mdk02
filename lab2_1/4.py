# Создаем функцию с параметром nums, которая возвращает минимальную сумму соседних 2-х чисел в списке nums
def min_pair(nums):
    minimum = nums[0] * nums[1]  # Вводим переменную, которая вычисляет произведение значений двух первых элементов списка nums
    for i in range(1, len(nums)):  # Создаем цикл for с функцией range; он будет проходиться по всем элементам nums в диапазоне от 2 элемента до конца списка
        # Обновляем переменную minimum; с помощью функции min выбирается минимум между суммой текущего и предыдущего значения элементов и текущим значением minimum
        minimum = min(nums[i] + nums[i - 1], minimum)
    # Возврат минимальной суммы соседних 2-х чисел
    return minimum

# Глобальная программа
# Импорт библиотеки random
import random
# С помощью функции seed генерируем одинаковые случайные значения при каждом запуске
# random.seed(50)
# Вводим переменные: количество случайных чисел(10), минимальное значение для диапазона чисел(1), максимальное значение для диапазона чисел(100)
N_MAX = 10
RANGE_MIN = 1
RANGE_MAX = 100
# Вводим переменную, в которой хранится список, сгенерированных случайным образом чисел от 1 до 100
nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)
# Вывод списка nums
print(nums)
# Вызов функции min_pair с аргументом nums; вывод минимальной суммы соседних 2-х чисел списка nums
print(min_pair(nums))


# # Создаем функцию с параметром nums, которая по условию задания должна возвращать минимальную сумму соседних 2-х чисел в списке nums
# def min_pair(nums):
#     min = nums[0] * nums[1] # Вводим переменную, которая вычисляет произведение значений двух первых элементов списка nums
#     for i in range(2, len(nums)): # Создаем цикл for с функцией range; он будет проходиться по всем элементам nums в диапазоне от 3 элемента до конца списка
# # Обновляем переменную min; с помощью функции min по условию задачи должен выбраться минимум между суммой тек. и след. значения элементов и текущим значением min
#         min = min(nums[i] + nums[i + 1], min)
#     # Возврат переменной min, в которой по условию задачи хранится минимальная сумма соседних 2-х чисел
#     return min



