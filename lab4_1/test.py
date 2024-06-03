import unittest  # импорт модуля unittest
# импорт функций из пакета figure
from figure import circle_perimeter, circle_area, square_perimeter, square_area, triangle_perimeter, triangle_area


class TestFigures(unittest.TestCase):  # объявление класса TestFigures, наследуемого от unittest.TestCase
    def test_circle_perimeter(self):  # тест проверки функции circle_perimeter с заданным радиусом
        self.assertEqual(circle_perimeter(2.2), 13.82)

    def test_circle_perimeter_default(self):  # тест проверки функции circle_perimeter с дефолтным радиусом
        self.assertEqual(circle_perimeter(), 31.42)

    def test_circle_area(self):  # тест проверки функции circle_area с заданным радиусом
        self.assertEqual(circle_area(3), 28.27)

    def test_circle_area_default(self):  # тест проверки функции circle_area с дефолтным радиусом
        self.assertEqual(circle_area(), 78.54)

    def test_square_perimeter(self):  # тест проверки функции square_perimeter с заданной стороной
        self.assertEqual(square_perimeter(100000000000), 400000000000)

    def test_square_perimeter_default(self):  # тест проверки функции square_perimeter с дефолтной стороной
        self.assertEqual(square_perimeter(), 60)

    def test_square_area(self):  # тест проверки функции square_area с заданной стороной
        self.assertEqual(square_area(5), 25)

    def test_square_area_default(self):  # тест проверки функции square_area с дефолтной стороной
        self.assertEqual(square_area(), 225)

    def test_triangle_perimeter(self):  # тест проверки функции triangle_perimeter с заданными сторонами
        self.assertEqual(triangle_perimeter(2, 3.9, 4), 9.9)

    def test_triangle_perimeter_default(self):  # тест проверки функции triangle_perimeter с дефолтными сторонами
        self.assertEqual(triangle_perimeter(), 17)

    def test_triangle_area(self):  # тест проверки функции triangle_area с заданными сторонами
        self.assertEqual(triangle_area(3, 7, 5.234), 7.19)

    def test_triangle_area_default(self):  # тест проверки функции triangle_area с дефолтными сторонами
        self.assertEqual(triangle_area(), 6.44)


if __name__ == '__main__':  # запуск тестов, если файл запущен как основной
    unittest.main()
