
def digit(a) -> bool:
    while a.replace("-","").replace(".","").isdigit():
        return True
    else:
        print(f"'{a}' не может быть координатой точки. Попробуйте еще раз")
        return False

while True:
    x1 = input("Введите x: ")
    if digit(x1):
        break
while True:
    y1 = input("Введите y: ")
    if digit(y1) == True:
        break

x = float(x1)
y = float(y1)
if x < 0 and y > 0:
    print("2 четверть")
elif x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
elif x > 0 and y < 0:
    print("4 четверть")
else:
    print("0 не входит в координатную плоскость. Попробуйте еще раз")
