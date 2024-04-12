import math


def check_digit(i):
    if i.replace(".","").replace("-","").isdigit():
        return True
    else:
        print(f"'{i}' не является числом. Попробуйте еще раз")


def formula(a1,b1,c1):
    a = float(a1)
    b = float(b1)
    c = float(c1)
    u = (((8 + ((math.fabs(a - b)) ** 2) + 1) ** (1/3)) / ((a ** 2) + (b ** 2) + 2)) - math.exp(math.fabs(a - b)) * (((math.tan(c)) ** 2) + 1) ** a
    print(f"u = {round(u, 2)}")


while True:
    x = input("Введите x: ")
    if check_digit(x):
        break

while True:
    y = input("Введите y: ")
    if check_digit(y):
        break

while True:
    z = input("Введите z: ")
    if check_digit(z):
        break

formula(x,y,z)