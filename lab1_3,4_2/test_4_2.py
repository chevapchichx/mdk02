import unittest  # импортируем модуль unittest
from code import *  # из модуля code импортируем все функции


class TestCode(unittest.TestCase):  # объявление класса TestCode, наследуемого от unittest.TestCase
    def test_1_check_digit(self):  # тест проверки функции check_digit_1
        self.assertEqual(check_digit_1("4347374873453"), True)
        self.assertEqual(check_digit_1("255123253f"), False)

    def test_1_check_zero(self):  # тест проверки функции check_zero_1
        self.assertEqual(check_zero_1(0), False)
        self.assertEqual(check_zero_1(123), True)

    def test_1_get_square(self):  # тест проверки функции get_square_1
        self.assertEqual(get_square_1(12, 7.3, 8), 28.43)
        self.assertEqual(get_square_1(5, 5, 5), 10.83)

    def test_1_get_type(self):  # тест проверки функции get_type_1
        self.assertEqual(get_type_1(5, 5, 5), "Равносторонний")
        self.assertEqual(get_type_1(5, 5, 6), "Равнобедренный")
        self.assertEqual(get_type_1(3, 4, 5), "Разносторонний")


    def test_3_check_zero(self):  # тест проверки функции check_zero_3
        self.assertEqual(check_zero_3(0), False)
        self.assertEqual(check_zero_3(1234), True)

    def test_3_get_square(self):  # тест проверки функции get_square_3
        self.assertEqual(get_square_3(20, 20, 20), 173.21)
        self.assertEqual(get_square_3(4, 7.9, 9), 15.79)

    def test_3_get_type(self):  # тест проверки функции get_type_3
        self.assertEqual(get_type_3(5, 5, 9), "Тупоугольный")
        self.assertEqual(get_type_3(6, 6, 6), "Остроугольный")
        self.assertEqual(get_type_3(5, 12, 13), "Прямоугольный")





