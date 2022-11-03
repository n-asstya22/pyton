#ZeroDivisionError
#x = 5/0

#TypeError
#x = "а" + 15

#IndexError
#x = [0, -15, "Антон"]
#x[3]

#SyntaxError
#x = "Привет,я Настя.

#SyntaxError
# if 5==4
#     print()

#NameError
# x = "Я строчка"
# print(x2)

#assert ---> AssertionError





#try - попытаться
#except - отлавливание оштбок
#finally - выполнить в любом случае
#else - иначе, если ошибок не было
#pass - "затычка",ничего не произойдет
#raise - вызвать ошибку
#as - сохранить ошибку в error_message

# try:
#     number = int(input())
#     x = 5 / number
# except ValueError:
#     print("Хочу цифры")
# except ZeroDivisionError: #любая ошибка будет обработана
#     print("Нельзя делить на нуль")
# except Exception:
#     print("Блин, ты ошибся, получается")
# else: # когда все хорошо🤗
#     print("Я подерил🦧")
# finally:
#     print("Меня написала Настя.Все права защищены.")
#
#
# print("Я закончил работать ")

#PASS
# try:
#     number = int(input())
#     x = 5 / number
# except Exception:
#     pass
# if 5 == 5:
#     pass  #TODO: дописать
#
# try:
#     x = input("Введи имя:")
#     if x == "Антон":
#         raise Exception("Антона в обиду не дам")
# except Exception as error_message :
#     print()

inst = []
try:
    f = open("text.txt")
except FileNotFoundError:
    print("Ну, не получилось")
else:
    try:
        for line in f:
            inst.append(int(line))
    except ValueError:
        print("Тут не число")
    else:
        print(inst)
    finally:    #вообще в любом случае
        f.close()
        print("Я закончил файл")