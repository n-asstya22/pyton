import random
import easygui
# class Chelovek:
#     pi = 3.14 # public статический
#     __city = "Новосибирск"  # private статический
#     def __init__(self):
#         self.h = 234 #public динамический
#         self.__vozrast = 99 #private динамический
#
# obj = Chelovek()
# print(obj.h)
# # print(Chelovek.pi)
# class Chelovek:
#     def __init__(self,hight=200): #значение по умолчанию
#         self.hi = hight
#
# obj = Chelovek()
# print(obj.hi)
class Human:
    default_name = "***"
    default_age = 345
    def __init__(self,name = default_name,age =default_age):
        self.n = name
        self.a = age
        self.__money = 100_000
        self.__house = False
    def earn_money(self):
        self.__money += 10_000
        return self.__money

    def __make_deal(self,h):
        if self.__money > h.final_price():
            self.__money -= h.final_price()
            return True

    def buy_house(self,h):
        if self.__make_deal(h):
            h.own = self.n
            self.__house = h

            return "дом куплен"
        else:
            return f"не хватает {h.final_price()-self.__money}"
    def info(self):
        return self.n,self.a, self.__money, self.__house
    def default_info(self):
        # self.n = Human.default_name
        # self.a = Human.default_age
        # return self.n,self.a
        return Human.default_name,Human.default_age
class House:
        area = "Новосибирск"
        price = 800_000
        def __init__(self, price_h = price,area_h = area):
            self.price = price_h
            self.area= area_h
            self.__scidka = random.randint(0, 25)

        def final_price(self,price_h = price,area_h = area):

            fin = price_h - (price_h * self.__scidka * 0.01)
            return fin

p = Human()
h = House()
h_1 = House(600_000,"Томск")
h_2 = House(400_000,"Искитим")
# print(h.final_price())
# print(h_1.final_price())
# print(h_2.final_price())
# a = print(p.buy_house(h))
a = easygui.indexbox(
    msg="Какой дои хотите в Нск,в Томске",
    choices = ('в Нск','в Томске','в Искитиме'))
if a == 0:#доделать easygui
    easygui.msgbox(p.buy_house(h))
    if "не хватает " in p.buy_house(h):
        b = easygui.indexbox(
            msg="Заработать или выйти?",
            choices=('Заработать ', 'Выйти'))
        if b == 0:
                p.earn_money()
if a == 1:
    easygui.msgbox(p.buy_house(h_1))
if a == 2:
    easygui.msgbox(p.buy_house(h_2))



#print(p.info())
#print(p.earn_money())
#print(h_1.final_price(400_000,"Томск"))
# print(p.default_info())

