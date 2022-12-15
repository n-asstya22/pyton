# МНОЖЕСТВА
# # set
# s = set() #пустое множество
# s1 = {1, 2, 3, 3} #повторения исключаются
# print(s1)
# s2 = {'A', 'Б', 'B'} #это неупорядоченный тип данных
# print(s2)
# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# print(s1.union(s2)) # обьединение
# print(s1 | s2) # обьединение

# print(s1.intersection(s2)) # пересечение
# print(s1 & s2) # пересечение

# print(s1.difference(s2)) # разность
# print(s1 - s2) # разность

# print(s1.symmetric_difference(s2)) # симметрическая разность
# print(s1 ^ s2)


#CЛОВАРИ
# d = {} #пустой словарь
# d1 = {'Пи': 3.14,
#       'Преподаватель': 'Aнтон',
#       'Список дел': ['Выжить', 'ловить балдеж']}
#
# print(d1['Преподаватель'])
# print(d1['Список дел'][1])



# from random import randint
# lst = []
# for _ in range (5):
#     randint(1,5)
#     lst.append(randint(1,5))
# print(lst)
# unique = set(lst)
# print(unique)
#
# print(f"{len(unique)} штук: {unique}")


#
# from random import randint
#
# lst1 = []
# lst2 = []
#
# size = randint(100, 1000)
# r_start = 0
# r_end = 10_000 #декоративный разделитель
# for _ in range(size):
#     lst1.append(randint(r_start,r_end))
#     lst2.append(randint(r_start, r_end))
# set1 = set(lst1)
# set2 = set(lst2)
#
# inter = set1.intersection(set2)
# print(f"Общих чисел: {len(inter)}")
# print(f"Кол-во генераций: {size}")
# print(f"Минимальное значение: {min(inter)}")
# print(f"Максимальное значение: {max(inter)}")
# # возможное решение,но простое
# inter1 = list(inter)
# inter1.sort()
# print(inter1)
# print(sorted(inter)) # sorter - преобразует в список и сортирует

set1 = set()
insert = ""
while insert != "end":
    insert = input("Ввод: ")
    if insert.lstrip("-").isdigit(): #убирпет символ слева
        if insert not in set1:
            print("Нет")
            set1.add(insert)
        else:
            print("Да")
    elif insert == "end":
        break
    else:
        print("Нужно число")



