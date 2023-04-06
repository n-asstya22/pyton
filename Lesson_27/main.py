# n = float(input("Введите число для округления"))
# def o(n):
#     if n % 1 >= 0.5:
#         n += 1
#         print(n)
#     else:
#         print(n)
#полтора землекопа
#1
# from math import ceil
# f = float(input("Введите число для округления"))
# print(ceil(f))

#2
# f = float(input("Введите число для округления"))
# def o(n):
#     if n % 1 > 0:
#         n = n // 1 + 1
#         print(n)
#     else:
#         print(n // 1)
#
#o(f)
#таск_лессон
#1
# c1 = input('Первый цвет:').lower().strip(" ")
# c2 = input('Второй цвет:').lower().strip(" ")
# cs = ("синий", "желтый", "красный ")
# if c1 not in cs or c1 not in cs:
#     print("Введен неправильный цвет")
# elif (c1 == cs[0] and c2 == cs[1]) or c1 == cs[1] and c2 == cs[0]:
#     print("Зеленый")
# elif (c1 == cs[1] and c2 == cs[2]) or c1 == cs[2] and c2 == cs[1]:
#     print("Оранжевый")
# elif (c1 == cs[0] and c2 == cs[2]) or c1 == cs[2] and c2 == cs[0]:
#     print("Фиолетовый")
# else:
#     print(c1.capitalize())

#2
s = input("Начало первого урока (чч:мм):")
l = int(input("Длительность урока (мин):"))
b = int(input("Длительность перемен (мин):"))
n = int(input("На сколько уроков расписание(мин):"))
splited_st = s.split(":")
sh = int(splited_st[0])
sm = int(splited_st[1])
time = sh * 60 + sm

for i in range(4):
    print(f"Урок {i + 1}: ", end="")
    print(f"{str(time // 60).rjust(2,'0')}:{str(time % 60).rjust(2,'0')} - ", end="")
    time += l
    print(f"{str(time // 60).rjust(2, '0')}:{str(time % 60).rjust(2, '0')} ")
    time += b
