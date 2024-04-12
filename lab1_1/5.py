#Создаем функцию для проверки введенных пользователем данных
def digit(a,b):
    # Если введенные данные являются числом, возвращается значение True
    while a.replace("-","").replace(".","").isdigit() and b.replace("-","").replace(".","").isdigit():
        return True
    # Если введенные данные не являются числом, возвращается значение False
    else:
        print(f"'{a}' не может быть координатой точки. Попробуйте еще раз")
        return False

# Вводим переменные x1 и y1
x1 = input("Введите x: ")
y1 = input("Введите y: ")

while digit(x1,y1) == True: # Пока функция digit возвращает значение True (то есть пока выполняется условие с 4 строки):
    x = float(x1) # Преобразовываем переменную x1 из str в float
    y = float(y1) # Преобразовываем переменную y1 из str в float
# Используя конструкцию if-elif-else, проверяем переменные, введенные пользователем
    # Если переменная x меньше 0 и переменная y больше 0
    if x < 0 and y > 0:
        print("2 четверть")
    # Если переменная x больше 0 и переменная y больше 0
    elif x > 0 and y > 0:
        print("1 четверть")
    # Если переменная x меньше 0 и переменная y меньше 0
    elif x < 0 and y < 0:
        print("3 четверть")
    # Если переменная x больше 0 и переменная y меньше 0
    elif x > 0 and y < 0:
        print("4 четверть")
    # Если переменные не проходят проверку ни по одному условию
    else:
        print("0 не входит в координатную плоскость. Попробуйте еще раз")
    break # Используем оператор break для прерывания цикла while-true, иначе цикл будет бесконечным
