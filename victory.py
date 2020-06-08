# Коментарий указан в формате: Знаменитость - год рождения
# А.Эйнштейн - 1879
# Галилей - 1564
# Чарльз Дарвин - 1809
# Томас Эдисон - 1847
# Зигмунд Фрейд - 1856
# Вильгельм Рентген - 1845
# Петр I - 1672
# Генри Форд - 1863
# Билл Гейтс - 1955
# Илон Маск - 1971

cor = int(0)
uncor = int(0)
answer = None

while answer != "нет":
    year = int(input("Введите год рождения А.Эйнштейна: "))
    if year == 1879:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Галилея: "))
    if year == 1564:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Чарльза Дарвина: "))
    if year == 1809:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Томаса Эдисона: "))
    if year == 1847:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Зигмунда Фрейда: "))
    if year == 1856:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Вильгельма Рентгена: "))
    if year == 1845:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Петра I: "))
    if year == 1672:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Генри Форда: "))
    if year == 1863:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Билла Гейтса: "))
    if year == 1955:
        cor += 1
    else:
        uncor += 1

    year = int(input("Введите год рождения Илона Маска: "))
    if year == 1971:
        cor += 1
    else:
        uncor += 1

    corper = cor * 100 / 10
    uncorper = uncor * 100 / 10
    print("Викторина окончена! Количество правильных ответов:", cor, ",а неправильных:", uncor)
    print("В процентном соотношении правильных:", corper, "%, неправильных:", uncorper, "%")
    cor = int(0)
    uncor = int(0)
    answer = input("Хотите сыграть ещё раз (да/нет)?: ")
else:
    print("Спасибо за игру!")
