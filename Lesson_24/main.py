import string
import datetime
# class Nazvanie:
#     def __init__(self):
#      self.money = 1_000 # public
#
#      self.__zarplata = 2 #private
#     def bar(self):
#         if self.__zarplata > 4:
#             return True
#         else:
#             return False
#
#     def __sad(self):
#         print("Саня грустит")
#
#
# sanya = Nazvanie()
# print(sanya.money)
# #print(sanya.__zarplata) #private нельзя выводить
# # sanya.__zarplata = 10
# # print(sanya.__zarplata)
# # sanya.__zarplata += 10
# # print(sanya.__zarplata) #private нельзя изменять
# print(sanya.bar())
# sanya._Nazvanie__zarplata = 1_000_000
#

#Задача_1
# class Car:
#     def __init__(self):
#         pass
#
#
#
#     def zapusk(self):
#         print("Автомобиль заведен ")
#
#     def otkl(self):
#         print("Автомобиль заглушен")
#
#     def y (self, year):
#         print(self.year = year)
#
#     def t (self,type):
#         self.type = type
#
#     def c (self, color):
#         self.color = color
#
# car_1 = Car()
# print(car_1.y(1988))
# print(car_1.t("Легковая"))
# print(car_1.c("Синий"))
# (car_1.zapusk())
# print(car_1.otkl())

# задача2
# class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
#
# al = Alphabet("eng")
# al.print()
# al.letters_num()

#задача_3
class Clock:
    def __init__(self):
         self.__time = datetime.datetime.now().strftime("%H:%M:%S")
         #self.__time = "08:07:06"
         self.__h, self.__m, self.__s = self.__time.split(":")
         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)

    def hours(self):
        self.__h += 1

    def minutes(self):
        self.__m += 1

    def seconds(self):
        self.__s += 1

    def test_h(self):
        if self.__h > 23:
            self.__h = 0

    def test_m(self):
        if self.__m > 59:
            self.__m = 0

            self.__h += 1


    def vivod(self):
        print(f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}")


time_0 = Clock()
time_0.minutes()
# time_0.test_m()
time_0.vivod()









