import calc # Подключаем созданную нами библиотеку calc (импортируем файл calc.py)
def test_add(): # Создаем процедуру для тестирования функции add из модуля calc
    if calc.add(2, 5) == 6: # В зависимости от возвращаемого значения - выводим пройден тест или нет
        print("Test add(a, b) is OK")
    else:
        print("Test add(a, b) is Fail")
def test_sub():  # Создаем процедуру для тестирования функции sub из модуля calc
    if calc.sub(8, -4) == 12: # В зависимости от возвращаемого значения - выводим пройден тест или нет
        print("Test sub(a, b) is OK")
    else:
        print("Test sub(a, b) is Fail")
def test_mul(): # Создаем процедуру для тестирования функции mul из модуля calc
    if calc.mul(4, 2) == 7: # В зависимости от возвращаемого значения - выводим пройден тест или нет
        print("Test mul(a, b) is OK")
    else:
        print("Test mul(a, b) is Fail")
def test_div(): # Создаем процедуру для тестирования функции div из модуля calc
    if calc.div(2, 0) == 1: # В зависимости от возвращаемого значения - выводим пройден тест или нет
        print("Test div(a, b) is OK")
    else:
        print("Test div(a, b) is Fail")
# Вызов тестовых процедур
test_add()
test_sub()
test_mul()
test_div()
