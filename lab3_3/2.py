# Создаем функцию print_order, которая выводит отсортированные данные в словаре
def print_order(*order, **info):
    print("Музыкальная библиотека №1\n") # Вывод сообщения
    for key, value in sorted(info.items()): # Перебор, сортировка и вывод элементов в словаре info: ключ - key, значение - value
        print(key, ":", value)
    print("Вы выбрали:") # Вывод сообщения
    for item in order: # Цикл for проходит по каждому элементу в кортеже order и выводит его
        print("  -", item)
    print("\nПриходите еще!") # Вывод сообщения
# Вызов функции print_order с передачей нескольких музыкальных произведений в качестве позиционных и ФИО с датой рождения в качестве именованных аргументов
print_order("Славянский марш", "Лебединое озеро", "Спящая красавица",
            "Пиковая дама", "Щелкунчик",
            author="П.И. Чайковский", birthday="07/05/1840")

# -------------
# Пример вывода:
#
# Музыкальная библиотека №1
#
# author : П.И. Чайковский
# birthday : 07/05/1840
# Вы выбрали:
#   - Славянский марш
#   - Лебединое озеро
#   - Спящая красавица
#   - Пиковая дама
#   - Щелкунчик
#
# Приходите еще!

# При упаковке аргументов все переданные позиционные аргументы
# будут собраны в кортеж 'order', а ключевые - в словарь 'info'

# def print_order(*order, **info):
#     print("Музыкальная библиотека №1\n")
#
#     # Словарь 'info' должен содержать ключи 'author' и 'birthday'
#     for key, value in sorted(info.item()):
#         print(key, ":", value)
#
#     # Кортеж 'order' содержит все наименования произведений
#     print("Вы выбрали:")
#     for item in order:
#         print("  -", item)
#
#     print("\nПриходите еще!")
#
# print_order("Славянский марш", "Лебединое озеро", "Спящая красавица",
#             "Пиковая дама", "Щелкунчик",
#             author="П.И. Чайковский", birthday="07/05/1840")

# -------------
# Пример вывода:
#
# Музыкальная библиотека №1
#
# author : П.И. Чайковский
# birthday : 07/05/1840
# Вы выбрали:
#   - Славянский марш
#   - Лебединое озеро
#   - Спящая красавица
#   - Пиковая дама
#   - Щелкунчик
#
# Приходите еще!