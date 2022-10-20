
# x = int(input("Введите число:"))
#
# if 5 < x < 10:  # двойное неравенство
#     print("Ура")
# if x < 10 and x > 5:  # два обязательных условия
#     print("Ура")
# if x < 10 or x > 5:
#     print("Ура")


 #списки

# name_1 = "жираф"
# name_2 = "лев"
# name_3 = "антилопа"
# animales = [name_1 , name_2 , name_3]
# animales.append("гиена")
#
# animales.pop()    #удалить по индексу
# animales.remove("лев")    #удалить по значению
# print(animales)

# индексация несколько раз
# man = [["антон" , "гриша"],["компьютеры", "настолки"],["мама"]]
# print(man[0][1])

#
# number =float(input("Введите число:"))
#
# if number < 0 :                  #если
#      print("отрицательное")
# elif number > 0 :                 #иначеесли
#      print("положительное")
# else:
#     print("у нас ноль ")          #иначе
#



# year = int(input("Введмте год:"))
# if year  % 4 == 0 аnd (year % 400 == 0 or year % 100 !=  0 ):
#     print("Високосный")
# else:
#     print("Не високосный")
#
# number_1 = int(input("Введите первое число:"))
# operation = input("Введите операцию (+ , - , / , * ,| ):").strip()
# number_2 = int(input("Введите второе число:"))
# lst = ["+", "-", "/", "*", "|"]
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     elif operation == "|":
#         print(abs(number_1) , abs(number_2))
                                                           #abc вывести модуль числа
# number_1 = int(input("Первое число:"))
# number_2 = int(input("Второе число:"))
# number_3 = int(input("Третье число:"))
#
# lst = [number_1, number_2, number_3]
# print("Максмимальное число:", max(lst))
# print("Минимальное число:", min(lst))
# #max максимальное число
# #min минимальное число
ticket = input("Введите номер билета:")
if len(ticket) == 6 and ticket.isdigit():
    first_half = ticket[:3]        #первые три число
    last_half = ticket [-3:]       #последние три числа
    first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    last_sum = int(last_half[-1]) + int(last_half[-2]) + int(last_half[-3])
    if first_sum == last_sum:
        print("Удачный билет \(￣︶￣*\))")
    else:
        print("Неудачный билет ⊙﹏⊙∥")
else:
    print("Фигня")