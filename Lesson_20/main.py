#f = open("fail.txt","w",encoding="utf-8")
# f.write("hello word\n")
# f.write("movavi")
#
# f.close()
# f = open("fail.txt","r")
# #content = f.read() #тение в одну строку.ЛИБО ТАК
# content = f.readlines() #чтение в одну строку.ЛИБО ТАК
# print(content)
# print(f"Первая строка:{content[0]}")
#
# for line in content:
#     print(line.rstrip()) #убирает пренос строки в конце строки
#
# f.close()
#Задача 1

# a = input("Введите имя файла:") #моя попытка
# print("Введите строку:")  #моя попытка
# f = open(a, "w")  #моя попытка
# s = ""    #моя попытка
# add = input() #моя попытка
#
# if add == " ":    #моя попытка
#     f.write(s)    #моя попытка
# else: #моя попытка

#
#     print("Файл записан")     #моя попытка
#
#
#
# f.close()     #моя попытка
# name = input("Ведите имя файла:")
# text = input(">")
# f = open(name, "w", encoding="utf-8")
# while text != "":
#      f.write(text + "\n")
#      text = input(">")
# f.close()
# print("Файл записан")

# f = open("fail.txt","r",encoding="utf-8")
# content = f.readlines() #чтение в одну строку.ЛИБО ТАК
# f.close()
# f = open("zad2.txt","w",encoding="utf-8") #вывод
# count = 1
#
# for line in content: #по каждой строке
#     result = f"{count}) {line}"
#     f.write(result)
#     count += 1
# print(content)


#Задача 4
n = int(input("N = "))
f = open("zad2.txt", "r", encoding="utf-8")
elements = f.readlines()
f.close()

a = elements[:n]
for elements in a:
    print(elements.rstrip())

