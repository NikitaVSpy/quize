year = None
day = None

while year != 1799:
    year = int(input("Введите год рождения А.С. Пушкина: "))
    if year != 1799:
        print("Неверный ответ")

while day != 06.06:
    day = float(input("Введите день рождения А.С. Пушкина (чч.мм): "))
    if day != 06.06:
        print("Неверный ответ")
else:
    print("Всё верно")
