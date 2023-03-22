import random
#задача "кафемашина"
# zapas = {"Вода": 750,
#          "Moлоко": 500,
#          "Кофе": 80,
#          "Деньги": 0
#          }
# class Latte:
#     def __init__(self):
#         pass
#     def vichet(self):
#         zapas["Вода"] -= 200
#         zapas["Moлоко"] -= 150
#         zapas["Кофе"] -= 24
#         zapas["Деньги"] += 50
# class Espresso:
#     def __init__(self):
#         pass
#     def vichet(self):
#         zapas["Вода"] -= 50
#         zapas["Moлоко"] -= 0
#         zapas["Кофе"] -= 18
#         zapas["Деньги"] += 35
# class Capuc:
#     def __init__(self):
#         pass
#     def vichet(self):
#         zapas["Вода"] -= 250
#         zapas["Moлоко"] -= 50
#         zapas["Кофе"] -= 24
#         zapas["Деньги"] += 45
# class o:
#     def otchet(self):
#         print(f"Вода:{zapas['Вода']} \n"
#               f"Moлоко:{zapas['Moлоко']} \n"
#               f"Кофе:{zapas['Кофе']} \n"
#               f"Деньги:{zapas['Деньги']}\n")
#
# while True:
#     a = input("Выбери одно из: латте/эспрессо/капучино:")
#     if a == "отчет" or a == " отчет" or a == "Отчет" or a == " Отчет":
#         zakaz = o()
#         zakaz.otchet()
#     #латте
#     elif a == "латте" or a == " латте" or a == "Латте" or a == " Латте":
#         if zapas["Вода"] >= 200 and zapas["Moлоко"] >= 150 and zapas["Кофе"] >=24:
#             print("Пожалуйста внесите оплату в размере 50руб")
#             vneseno = input("Оплата(руб) или выход :")
#             if vneseno == "выход":
#                 False
#             else:
#                 vneseno = int(vneseno)
#                 if vneseno < 50:
#                     print("Не хватает",50 - vneseno,"руб")
#                     d = input("Оплата(руб) или выход :")
#                     if d == "выход":
#                         False
#                     else:
#                         d = int(d)
#                         vneseno += d
#                         if vneseno == 50:
#                             zakaz = Latte()
#                             zakaz.vichet()
#                             print("Вот ваш латте")
#                         elif vneseno < 50:
#                             print("Не хватило средств")
#                             False
#                 elif vneseno == 50:
#                     zakaz = Latte()
#                     zakaz.vichet()
#                     print("Вот ваш латте")
#                 elif vneseno > 50:
#                     sd = vneseno - 50
#                     if sd > zapas["Деньги"]:
#                         print("к сожалению, сдача не может быть выдана. Заказ отменён.")
#                         False
#                     else:
#                         print("Ваша сдача:", vneseno - 50)
#                         zakaz = Latte()
#                         zakaz.vichet()
#         else:
#             print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
#             False
#     #эспрессо
#     elif a == "эспрессо" or a == " эспрессо" or a == "Эспрессо" or a == " Эспрессо":
#         if zapas["Вода"] >= 50 and zapas["Moлоко"] >= 0 and zapas["Кофе"] >= 18:
#             print("Пожалуйста внесите оплату в размере 35руб.")
#             vneseno = input("Оплата(руб) или выход :")
#             if vneseno == "выход":
#                 False
#             else:
#                 vneseno = int(vneseno)
#                 if vneseno < 35:
#                     print("Не хватает", 35 - vneseno, "руб")
#                     d = input("Оплата(руб) или выход :")
#                     if d == "выход":
#                         False
#                     else:
#                         d = int(d)
#                         vneseno += d
#                         if vneseno == 35:
#                             zakaz = Espresso()
#                             zakaz.vichet()
#                             print("Вот ваш латте")
#                         elif vneseno < 35:
#                             print("Не хватило средств")
#                             False
#                 elif vneseno == 35:
#                     zakaz = Espresso()
#                     zakaz.vichet()
#                     print("Вот ваш латте")
#                 elif vneseno > 35:
#                     sd = vneseno - 35
#                     if sd > zapas["Деньги"]:
#                         print("к сожалению, сдача не может быть выдана. Заказ отменён.")
#                         False
#                     else:
#                         print("Ваша сдача:", vneseno - 35)
#                         zakaz = Espresso()
#                         zakaz.vichet()
#             # zakaz = Espresso()
#             # zakaz.vichet()
#             # #oplata = int(input("Оплата(руб):"))
#             # print("Вот ваш эспрессо")
#         else:
#             print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
#             False
#     #капучино
#     elif a == "капучино" or a == " капучино" or a == "Капучино" or a == " Капучино":
#         if zapas["Вода"] >= 250 and zapas["Moлоко"] >= 50 and zapas["Кофе"] >= 24:
#             print("Пожалуйста внесите оплату в размере 45руб.")
#             vneseno = input("Оплата(руб) или выход :")
#             if vneseno == "выход":
#                 False
#             else:
#                 vneseno = int(vneseno)
#                 if vneseno < 45:
#                     print("Не хватает", 45 - vneseno, "руб")
#                     d = input("Оплата(руб) или выход :")
#                     if d == "выход":
#                         False
#                     else:
#                         d = int(d)
#                         vneseno += d
#                         if vneseno >= 45:
#                             zakaz = Capuc()
#                             zakaz.vichet()
#                             print("Вот ваш капучино")
#                         elif vneseno < 45:
#                             print("Не хватило средств")
#                             False
#                 elif vneseno == 45:
#                     zakaz = Capuc()
#                     zakaz.vichet()
#                     print("Вот ваш капучино")
#                 elif vneseno > 45:
#                     sd = vneseno - 45
#                     if sd > zapas["Деньги"]:
#                         print("к сожалению, сдача не может быть выдана. Заказ отменён.")
#                         False
#                     else:
#                         print("Ваша сдача:", vneseno - 45)
#                         zakaz = Capuc()
#                         zakaz.vichet()
#             # zakaz = Capuc()
#             # zakaz.vichet()
#             # #oplata = int(input("Оплата(руб):"))
#             # print("Вот ваш капучино")
#
#
#         else:
#             print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
#             False
#
#
#     elif a == "":
#
#         break

#задача на 23.03.2022

class Anim: #создание самого класса


    def chist(self, chistota, nastroi, sitost):
        chistota += 10
        nastroi -= 5
        sitost -= 5
        if chistota > 100:
            chistota = 100
        elif chistota < 0:
            chistota = 0
        if nastroi > 100:
            nastroi = 100
        elif nastroi < 0:
            nastroi = 0
        if sitost > 100:
            sitost = 100
        elif sitost < 0:
            sitost = 0


        return chistota, nastroi, sitost

    def nast(self, chistota, nastroi, sitost):
        chistota -= 5
        nastroi += 10
        sitost -= 5
        if chistota > 100:
            chistota = 100
        elif chistota < 0:
            chistota = 0
        if nastroi > 100:
            nastroi = 100
        elif nastroi < 0:
            nastroi = 0
        if sitost > 100:
            sitost = 100
        elif sitost < 0:
            sitost = 0
        return (chistota, nastroi, sitost)

    def sit(self, chistota ,nastroi, sitost):
        chistota -= 5
        nastroi -= 5
        sitost += 10
        if chistota > 100:
            chistota = 100
        elif chistota < 0:
            chistota = 0
        if nastroi > 100:
            nastroi = 100
        elif nastroi < 0:
            nastroi = 0
        if sitost > 100:
            sitost = 100
        elif sitost < 0:
            sitost = 0
        return (chistota, nastroi, sitost)

    def otravlenie(self,chistota ,nastroi, sitost):
        chistota -= 0
        nastroi -= 15
        sitost -= 5
        if chistota > 100:
            chistota = 100
        elif chistota < 0:
            chistota = 0
        if nastroi > 100:
            nastroi = 100
        elif nastroi < 0:
            nastroi = 0
        if sitost > 100:
            sitost = 100
        elif sitost < 0:
            sitost = 0
        return (chistota, nastroi, sitost)

    def progulka(self,chistota ,nastroi, sitost):
        chistota -= 10
        nastroi += 15
        sitost -= 0
        if chistota > 100:
            chistota = 100
        elif chistota < 0:
            chistota = 0
        if nastroi > 100:
            nastroi = 100
        elif nastroi < 0:
            nastroi = 0
        if sitost > 100:
            sitost = 100
        elif sitost < 0:
            sitost = 0
        return (chistota, nastroi, sitost)


kot = Anim()
a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
# print(a,b,c)
# print(kot.chist(a,b,c))
# print(kot.nast(a,b,c))
# print(kot.sit(a,b,c))
# print(kot.otravlenie(a,b,c))
# # print(type(kot.progulka(a,b,c)))

d = input("Помыть/Поиграть/Покормить?")
lst = [d, d, d, d, "особое действие"]
d_1 = random.choice(lst)
if d_1 == "Помыть":

    print("Чистота,Настрой,Сытость:",kot.chist(a, b, c))


elif d_1 == "Поиграть":

    print("Чистота,Настрой,Сытость:",kot.nast(a, b, c))


elif d_1 == "Покормить":

    print("Чистота,Настрой,Сытость:",kot.sit(a, b, c))


elif d_1 == "особое действие":
        sob_list = [1,2]
        sob = random.choice(sob_list)
        #print(sob)
        if sob == 1:
            print("упс,тебе выпало неудачное особое действие:'Отравление'😢.-10 к настроению и - 5 к сытости")
            print("Чистота,Настрой,Сытость:",kot.otravlenie(a,b,c))


        if sob == 2:
            print("ура,тебе попалось особое действие:'Прогулка'!Ты получаешь +15 к настроению,но -10 чистоты")
            print("Чистота,Настрой,Сытость:",kot.progulka(a,b,c))















