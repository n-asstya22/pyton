# try:
#     number = int(input("Введите число:"))
# except (ValueError, IndexError):
#     print("Понятно")
# # except IndexError:
# #     print("ok")
# else: #если исключений не было
#     print("Нет исключений")
# finally:
#     print("Конец")
#
#
# name = input("Введите имя друга:").title()
# if name == "Анотон":
#     raise ValueError("не друг больше")
#
# except ValueError :
#     print("запрещено")

#задача 1
# def num(content):
#     s = 0
#     k = 0
#     for chisla in content:
#         try:
#             s += int(chisla)
#         except ValueError:
#             print("найдено не число", "'",chisla, "'")
#         else:
#             k += 1
#         if k == 0:
#             print("числа не найдены")
#             return("[здесь нет ничего] ")
#
#     return round(s/k, 3)
#
# try:
#     f = open("numbers.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет")
#     quit()
# content = f.read().split()
# f.close()
# print(num(content))

#задача 2
# try:
#      f = open("numbers.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#      print("файла нет")
#      quit()
# content = f.readlines()
# f.close()
# print(content)
#
#
#
# for i, student in enumerate(content):
#     content [i] = student.split()
#
#
# maxi = -1
# for student in content:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print("Неверно указан балл", student)
#     except IndexError:
#         print("Балл не указан", student)
#
#
# if maxi == -1:
#     print("Нет информации об участниках")
#     exit()
#
# print(maxi)

try:
    f = open("numbers.txt", "r", encoding="utf-8")
except FileNotFoundError:
     print("файла нет")
     quit()

content = f.read()
f.close()
word = input("Какое слово мы ищем:")
print(content.count(word))



