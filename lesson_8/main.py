#Первый способ
# import random
# number =  random.randint(0, 100)
#Второй способ
# import random as r
# numder  = r.randint(1, 100)
#Третий способ
# from random import randint
# number = randint(0, 100)
#Четвертый способ
# from  random import *
# numder = randint(1, 100)

# import turtle
#
# sreen = turtle.Screen()
# t = turtle.Turtle()
# hor = 200
# ver = 100
# t.pensize(9)
# t.width(9)
# t.color("purple", "light blue")
# t.speed(6)
#1- очень медленно
# 10 - очень быстро
# 0 - максимально быстро

# t.begin_fill()
# t.forward(hor)  #forward - вперед
# t.right(90)
# t.fd(ver) # = forward
# t.rt(90)
# t.fd(hor)
# t.rt(90)
# t.fd(ver)
# t.rt(90)
# t.end_fill()
#
# t.penup()
# t.goto(120, -30)
# t.pendown()
# t.fd(50)
#
# t.shape("turtle")
# t.begin_fill()
# t.color("purple", "light blue" )
# t.circle(30)
# t.end_fill()
#
# t.write("Movavi", font=("Arial", 50, "italic"))
#
# colors = ["red","orange","yellow","green","light blue","blue","purple"]
# angle = 360/7
# for img in range(0,7):
#     t.color(colors[img])
#     t.fd(80)
#     t.rt(angle)
#     print(img)
#
#
# sreen.exitonclick()

import random
import time
is_game = True
print("Время пострелять")
while is_game:
    print("Заряжаем патрон")
    time.sleep(2)
    print("Крутим барабан")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("*Выстрел*")

    slots = [1,2,3,4,5,6]
    patron = random.choice(slots)
    our = random.choice(slots)
    if patron == our:
        print("Есть пробитие 🥶")
        print("Смерть 💀")
        is_game = False
    else:
        print("Пробитие отсутсвует😇")
        a = input("Играть дальше? (да/нет)")
        if a == "нет":
            is_game = False
