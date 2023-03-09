from random import randint
# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return("я Кистина")
#
#
# evgenii = Person("Евгений",24)
# ann = Person(vozrast = 0, imya = "Кристина")
# print(ann.name)
# print(evgenii.age)

# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимания, что здесь нет print(), просто обращение по ключу
# hi[42]
# hi['Movavi']

#Задача 1, 2
# class Person:
#     def __init__(self, imya,vozrast , familia  ):
#         self.name = imya
#         self.age = vozrast
#         self.surename = familia
#         self.grates = [ randint(2,5) for n in range(randint(5,10))]
#         self.av_grate = sum(self.grates) / len(self.grates)
#     def __str__(self):
#         return f"{self.name} {self.surename} {self.age}"
#     def greet(self):
#         return f"Меня зовут {self.name} {self.surename},мне {self.age}"
#
# vladislav = Person("Владислав", 14,"Форвен")
# melania = Person("Mелания", 14, "Дорн")
# anton = Person("Антон",13,"Ветров")
# ann = Person("Аня",14 , "Путрова")
# # print(ann.name)
# # print(ann.age)
# # print(ann.surename)
# # print(ann)
# # print(ann.greet())
# # print(ann.grates)
# # print(ann.av_grate)
# students = [vladislav,melania,ann,anton]
# d = {}
#
# for i in students:
#     d[i.name] = i.av_grate
#
# sorted_d = dict(reversed(sorted(d.items(), key=lambda item: item[1])))
# print(sorted_d)
#
# for i in d:
#     print(i)

#Задача 2
class  Rectangle:
    def __init__(self,d1 , d2):
        self.dot1 = d1
        self.dot2 = d2
    def ploshad(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return a*b
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dot1 = Point(1, 152)
dot2 = Point(2, 254)
rectangle = Rectangle(dot1, dot2)
print(rectangle.ploshad())
