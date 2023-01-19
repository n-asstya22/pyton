
# def plus_one(a,b): #обьявление о функции с двумя аргуменами
#     return a+b+1
# print (plus_one(5,4))

# plus_one_2 = lambda a, b: a+b+1

# #if - else
# result = lambda answer:True if answer == "д" else False

#list comprehension
# spisok= []
# for i in range(1, 6):
#     spisok.append(1)
# print(spisok)
#
# spisok2 = [for i in range(1,6)]:
#
# #list comprehension пишется в []
# #for i in range(1,6)  - обычный цикл for --> ск раз повторяется
# #все,что слева от for --> элементы в списке
# print(spisok2)


# #1 задача
# c2f = lambda c:9/5 * c + 32
# f2c = lambda f:(f - 32)* 5/9
# c2k = lambda c:c + 273.15
# k2c = lambda k:k - 273.15
# f2k = lambda f:c2k(f2c(f))
# print(f2k(203))

#2 задача
#  from random import randint
#  l = lambda zxc:True if zxc == "Д" else False
# while True:
#     a = int(input("Сколько раз кидаем кубик?"))
#     dies = [randint (1,6)for i in range(a)]
#     print(dies)     b = input("Выходим? (Д/Н)").upper()
#     if l(b):# если игрок решил выйти
#          break
# #3 Задача
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#           list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#           list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#           list("abcdefghijklmnopqrstuvwxyz"),
#           list("1234567890")
#          ]
# a = [choice(choice(chars)) for i in range(6)]
# a2 = ("".join(a))
# d = {}
# link = "https://www.google.com"
# if link in d:
#     print("Ссылка уже есть в базе,вот код")
#     print(d[link])
# else:
#     print("Ссылка добавлена в базу,вот ее код")
#     d[link] = a2
4. Задача
u = lambda a, b:a / b
print(u(6,3))
u2 =lambda a, b:a % b
print(u2(6,3))
u3 = lambda a, b:a // b
print(u3(6,3))
u4 = lambda a, b:a**b
print(u4(6,3))
u5 =lambda a:-a if a < 0 else a #если число отрицательное,
#то меняем знак на противоположный
print(u5(-6))




