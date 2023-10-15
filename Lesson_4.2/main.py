import random
#ex1
# my_dict = {
# }
# def biggest_g(**kwargs):
#     my_dict.update(**kwargs)
#
#
# biggest_g(a=5,b=3,c=23)
# print(my_dict)
#Классы

# class Voin:
#     def __init__(self,name,health,damage,):
#         self.health = health
#         self.damage = damage
#         self.name = name
#     def hit(self,v):
#         v.health -= self.damage
#         print(f"Ударил {self.name},пострадал {v.name},у него осталось {v.health}")
#
#
# v1 = Voin("Воин 1",100, random.randint(20, 40))
# v2 = Voin("Воин 2",100, random.randint(20, 40))
# while v1.health > 0 and v2.health > 0:
#     if random.randint(1,2) == 1:
#         v1.hit(v2)
#     else:
#         v2.hit(v1)
#     if v1.health <= 0 or v2.health <= 0:
#         print("Game over")
#         break

#ex 7 Homework
class Rectangle:
    def __init__(self,ul,br):
        self.ul = ul
        self.br = br

class Point:
    def __init__(self,x,y):
        self.x = random.randint(-100,100)
        self.y = random.randint(-100,100)
        print(self.x,self.y)
def s(a,b):
    print(a*b)


p1 = Point(0,0)
p2 = Point(0,0)
r = Rectangle(p1,p2)

a = abs(p1.x-p2.x)
b = abs(p1.y-p2.y)
print(a,p1.x-p2.x)
print(b,p1.y-p2.y)
s(a,b)