# x = 7
# if x == 5: #False
#     print("Я не сработаю😢")
# else:      #Если не сработают if или elif
#     print("Я, вероятно сработаю :D")

# word_1 = input("Введите слово (1/2): ")
# word_2 = input("Введите слово (2/2): ")
#
# word_1 = word_1.lower()
# word_2 = word_2.lower()
#
# if word_1.isalpha() and word_2.isalpha()
#
#     sorted_w1 = sorted(word_1)
#     sorted_w2 = sorted(word_2)
#
#     print(sorted_w1)
#     print(sorted_w2)
#
#     if sorted_w1 == sorted_w2:
#         print("Ура,у вас анаграмма 🐹😊")
#     else:
#         print("Грустно")
# else:
#     print("хочу только буквы")

q1 = input("Сколько будет 2 + 2\n"
           "a) 4, б) 5, в) 3, г)6\n"
           "--> ")
if q1 == "а":
    print("Правильно 😎")
else:
    print("Одна ошибка и ты ошибся 🤦️")
    quit()

q2 = input("Арбуз - это ...?\n"
           "a)корнеплод, б)овощ, в)ягоды\n"
           "--->")
if q2 == "в":
    print("Правильно 😎")
else:
    print("Одна ошибка и ты ошибся 🤦️")
    quit()

q3 = input("Что такое цугцванг\n"
           "a)Положение в шашках и шахматах, в котором любой ход игрока ведёт к ухудшению его позиции.\n"
           "б)sırt çantası\n"
           "в)поджанр аниме , посвященный Егору\n"
           "г)порода обезьяны\n"
           "--->")
if q3 == "а":
    print("Ну как бы да, в общем-то ничего интересного")
elif q3 == "в":
    print("Партия гордится тобой, плюс вторая порциямиска риса")
else:
    print("Ну нет, правильный ответ `в`")
    quit()

print("Ты победил 😎😵")
