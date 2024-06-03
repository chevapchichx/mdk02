import unittest # Подключаем модуль для создания и запуска тестов
import calc # Подключаем созданную нами библиотеку calc (импортируем файл calc.py)
class CalcTest(unittest.TestCase): # Создаем класс CalcTest для проверки тест-модулей (наследник unittest.TestCase)
    # Создание тестовых методов для тестирования функций из модуля calc
    def test_add(self):  # Cоздание процедуры с параметром self для тестирования функции add из calc
        self.assertEqual(calc.add(1, 2), 3)
    def test_sub(self): # Cоздание процедуры с параметром self для тестирования функции sub из calc
        self.assertEqual(calc.sub(4, 2), 2)
    def test_mul(self): # Cоздание процедуры с параметром self для тестирования функции mul из calc
        self.assertEqual(calc.mul(2, 5), 10)
    def test_div(self): # Cоздание процедуры с параметром self для тестирования функции div из calc
        self.assertEqual(calc.div(8, 4), 2)
if __name__ == '__main__': # Запуск всех тест-модулей, определенных в классе CalcTest (в лучае запуска скрипта напрямую)
    unittest.main()
