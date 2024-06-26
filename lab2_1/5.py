# Создаем функцию с параметром nums, которая удаляет из списка nums отрицательные элементы и возвращает измененный список
def non_negatives(nums):
#Создаем цикл for с функцией range; он проходится по списку nums в обратном порядке, начиная с последнего элемента, потому что индексы элементов меняются после удаления
    for i in range(len(nums) - 1, -1, -1):
        # С помощью оператора if с условием, что элемент из nums < 0, находятся и удаляются все отрицательные значения элементов
        if nums[i] < 0:
            del nums[i]
    # Возврат измененного списка nums
    return nums

# Глобальная программа
# Импорт библиотеки random
import random
# Вводим переменную, в которой хранится кол-во сгенерированных чисел
n = 10
# Вводим переменную, в которой хранится список, сгенерированных случайным образом чисел от -10 до 10 с округлением до 2 знаков после запятой
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
# Вывод списка nums
print(nums)
# Вызов функции non_negatives с параметром nums
non_negatives(nums)
# Вывод списка nums
print(nums)

# # Создаем функцию с параметром nums, которая по условию задачи должна удалять из списка nums отрицательные элементы и возвращает измененный список
# def non_negatives(nums):
# #Создаем цикл for с функцией range; он проходится по списку nums; однако здесь присутсвует ошибка, из-за чего условие задачи не выполняется
#     for i in range(len(nums)):
#         # С помощью оператора if с условием, что элемент из nums < 0, находятся и удаляются все отрицательные значения элементов
#         if nums[i] < 0:
#             del nums[i]
#     # Возврат измененного списка nums
#     return nums