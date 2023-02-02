# #Словари
# d = {}      #пустой список
# d = dict()  #пустой список
#
# d = {"ключ1": 1,
#      10: "два",
#      True: "Ложь",
#      " ": 0,
#      "" : 2,
#      (1, 2, 3) : "e"}
#Функция
# def Hello_world() : #обьявление функции
#     print("hello_world")
#
# Hello_world() #вызов функций

# def funs (imya):
#     print("привет",imya)
#
# #-----------------------
# name = input("Ваше имя:")
# funs(imya=name) #вызов функции с аргуменом

# def s(chislo1, chislo2):
#     result = chislo1 + chislo2
#     return result #return = вернуть что-то из функции
#
# print(s(0,0)) #вывод результата функции(то что вернет return)
# x = s(5,2)

# def more_than_5(number):
#     if number>5:
#        return True
#
# more_5(8):#если выполниться
#     print("класс")
#

 #задача1
# def is_sorted(spisok):
#      ss = sorted(spisok)
#      if spisok == ss:
#          return True
#
#
#
# spisok = [1, 2, 5, 6, 78, 123]
# if is_sorted(spisok):
#     print("Ура,сортировано ")
# else:
#     print("Не сортировано")
 #задача2
# def find_lonest(n:list):
#     s1 = []
#     for img in n:
#         s1.append(len(img))
#     maxy = max(s1)
#     ind = s1.index(maxy) #нашли индекс maxy
#     return s[ind],maxy
#
# s = ["слон","кот","Россия"]
# print(find_lonest(s))
#задача3
# def min_max(spisok):
#
#     # min = min(spisok)
#     # max = max(spisok)
#     s = sorted(spisok)
#     mini = s[0] #минимум
#     maxi = s[-1] #максимум
#     return mini, maxi
# spisok = [17,213,23,3]
# print(min_max(spisok))
#Задача4
def is_prime(celogo_chislo):
    for i in range(2,celogo_chislo + 1):
        if i == celogo_chislo :
            return True
        if celogo_chislo % i == 0:
            break


if is_prime(37221):
    print("простое число")
else:
    print("НЕ простое число")