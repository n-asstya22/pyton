zapas = {"Вода": 750,
         "Moлоко": 500,
         "Кофе": 80,
         "Деньги": 0
         }
class Latte:
    def __init__(self):
        pass
    def vichet(self):
        zapas["Вода"] -= 200
        zapas["Moлоко"] -= 150
        zapas["Кофе"] -= 24
        zapas["Деньги"] += 50
class Espresso:
    def __init__(self):
        pass
    def vichet(self):
        zapas["Вода"] -= 50
        zapas["Moлоко"] -= 0
        zapas["Кофе"] -= 18
        zapas["Деньги"] += 35
class Capuc:
    def __init__(self):
        pass
    def vichet(self):
        zapas["Вода"] -= 250
        zapas["Moлоко"] -= 50
        zapas["Кофе"] -= 24
        zapas["Деньги"] += 45
class o:
    def otchet(self):
        print(f"Вода:{zapas['Вода']} \n"
              f"Moлоко:{zapas['Moлоко']} \n"
              f"Кофе:{zapas['Кофе']} \n"
              f"Деньги:{zapas['Деньги']}\n")

while True:
    a = input("Выбери одно из: латте/эспрессо/капучино:")
    if a == "отчет" or a == " отчет" or a == "Отчет" or a == " Отчет":
        zakaz = o()
        zakaz.otchet()
    #латте
    elif a == "латте" or a == " латте" or a == "Латте" or a == " Латте":
        if zapas["Вода"] >= 200 and zapas["Moлоко"] >= 150 and zapas["Кофе"] >=24:
            print("Пожалуйста внесите оплату в размере 50руб")
            vneseno = input("Оплата(руб) или выход :")
            if vneseno == "выход":
                False
            else:
                vneseno = int(vneseno)
                if vneseno < 50:
                    print("Не хватает",50 - vneseno,"руб")
                    d = input("Оплата(руб) или выход :")
                    if d == "выход":
                        False
                    else:
                        d = int(d)
                        vneseno += d
                        if vneseno == 50:
                            zakaz = Latte()
                            zakaz.vichet()
                            print("Вот ваш латте")
                        elif vneseno < 50:
                            print("Не хватило средств")
                            False
                elif vneseno == 50:
                    zakaz = Latte()
                    zakaz.vichet()
                    print("Вот ваш латте")
                elif vneseno > 50:
                    sd = vneseno - 50
                    if sd > zapas["Деньги"]:
                        print("к сожалению, сдача не может быть выдана. Заказ отменён.")
                        False
                    else:
                        print("Ваша сдача:", vneseno - 50)
                        zakaz = Latte()
                        zakaz.vichet()
        else:
            print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
            False
    #эспрессо
    elif a == "эспрессо" or a == " эспрессо" or a == "Эспрессо" or a == " Эспрессо":
        if zapas["Вода"] >= 50 and zapas["Moлоко"] >= 0 and zapas["Кофе"] >= 18:
            print("Пожалуйста внесите оплату в размере 35руб.")
            vneseno = input("Оплата(руб) или выход :")
            if vneseno == "выход":
                False
            else:
                vneseno = int(vneseno)
                if vneseno < 35:
                    print("Не хватает", 35 - vneseno, "руб")
                    d = input("Оплата(руб) или выход :")
                    if d == "выход":
                        False
                    else:
                        d = int(d)
                        vneseno += d
                        if vneseno == 35:
                            zakaz = Espresso()
                            zakaz.vichet()
                            print("Вот ваш латте")
                        elif vneseno < 35:
                            print("Не хватило средств")
                            False
                elif vneseno == 35:
                    zakaz = Espresso()
                    zakaz.vichet()
                    print("Вот ваш латте")
                elif vneseno > 35:
                    sd = vneseno - 35
                    if sd > zapas["Деньги"]:
                        print("к сожалению, сдача не может быть выдана. Заказ отменён.")
                        False
                    else:
                        print("Ваша сдача:", vneseno - 35)
                        zakaz = Espresso()
                        zakaz.vichet()
            # zakaz = Espresso()
            # zakaz.vichet()
            # #oplata = int(input("Оплата(руб):"))
            # print("Вот ваш эспрессо")
        else:
            print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
            False
    #капучино
    elif a == "капучино" or a == " капучино" or a == "Капучино" or a == " Капучино":
        if zapas["Вода"] >= 250 and zapas["Moлоко"] >= 50 and zapas["Кофе"] >= 24:
            print("Пожалуйста внесите оплату в размере 45руб.")
            vneseno = input("Оплата(руб) или выход :")
            if vneseno == "выход":
                False
            else:
                vneseno = int(vneseno)
                if vneseno < 45:
                    print("Не хватает", 45 - vneseno, "руб")
                    d = input("Оплата(руб) или выход :")
                    if d == "выход":
                        False
                    else:
                        d = int(d)
                        vneseno += d
                        if vneseno == 45:
                            zakaz = Capuc()
                            zakaz.vichet()
                            print("Вот ваш капучино")
                        elif vneseno < 45:
                            print("Не хватило средств")
                            False
                elif vneseno == 45:
                    zakaz = Capuc()
                    zakaz.vichet()
                    print("Вот ваш капучино")
                elif vneseno > 45:
                    sd = vneseno - 45
                    if sd > zapas["Деньги"]:
                        print("к сожалению, сдача не может быть выдана. Заказ отменён.")
                        False
                    else:
                        print("Ваша сдача:", vneseno - 45)
                        zakaz = Capuc()
                        zakaz.vichet()
            # zakaz = Capuc()
            # zakaz.vichet()
            # #oplata = int(input("Оплата(руб):"))
            # print("Вот ваш капучино")


        else:
            print("К сожелению, недостаточно ресурсов, кофемашина больше не работает")
            False


    elif a == "":
        break












