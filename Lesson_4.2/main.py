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

class Voin:
    def __init__(self,name,health,damage,):
        self.health = health
        self.damage = damage
        self.name = name
    def hit(self,v):
        v.health -= self.damage
        print(f"Ударил {self.name},пострадал {v.name},у него осталось {v.health}")


v1 = Voin("Воин 1",100, random.randint(20, 40))
v2 = Voin("Воин 2",100, random.randint(20, 40))
while v1.health > 0 and v2.health > 0:
    if random.randint(1,2) == 1:
        v1.hit(v2)
    else:
        v2.hit(v1)
    if v1.health <= 0 or v2.health <= 0:
        print("Game over")
        break