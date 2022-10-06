
# name_1="Жираф"
# name_2="Слон"
# name_3="Лвенок"
#
# friend = [name_1, name_2, name_3]
# print(friend)
# print(friend[0])
# print(friend[-3])
#
# alphabet = "АБВГДЕЁЖЗИКЛМН"
# print(alphabet[0])
# print(alphabet[-1])
# print(alphabet[0] + alphabet[1] + alphabet[2])
# print(alphabet[0:3])       #вывести 3 первых
# print(alphabet[-3:])       #вывести 3 последних
# print(alphabet[:6])
# print(alphabet[:6:2])      #вывести через одного среди первых шести чисел
# # [start:end:step]
#
# print(alphabet[::-1])  #вывести в обатном порядке
# print(alphabet[::-2])  #вывести в обратном порядке через одого
# х = input("Введи слово:")
# # print("Первая ибуква:", х [0])
# # print("Последняя буква:", х [-1])
# temp = х[-1]   #сохранили последний символ
# print(х.index(temp) + 1)  #индекс послнднего символа + 1
# print(len(х))

# Решение, но не крутое
# path = "С:/Python3/python.exe"
# temp = path.split("/")
# print(temp)
# print("Имя файла:",temp[-1])
# print("Расширение:", temp[-1][-3:] )
# print("Имя каталога:", temp[1])
# print("Полный путь к каталогу:",temp[0] + "/" +  temp[1])

chapter_1 = input("Глава 1 :")
page_1 = input("Страница :")

chapter_2 = input("Глава 2 :")
page_2 = input("Страница :")

print(chapter_1.ljust(15),page_1.rjust(15))
print(chapter_2.ljust(15),page_2.rjust(15))