# surename = input("Фамилия:").capitalize()
# imya = input("Имя:").capitalize()
# otchestvo = input("Отчество:").capitalize()
#
# print(surename, imya[0]+".", otchestvo[0]+".")
# print(f"{surename} {imya[0]}. {otchestvo[0]}.")

#
# word = input("Введи фразу/слово")
#  word.count("а")
# print("а:", word.count("а"))
# print("аb:", word.count("аb"))phrase = input("введите фразе")
# phrase = input("Введите фразу,разделенную пробелами:").strip()
# lst = phrase.split(" ")
# print(lst)
# lst.pop(0)   #удалить по индексу
# lst.remove("антона")   #удалить по значанию
#
# print(lst)
# phrase = input("Введите фразу:")
# find = input("Что меняем:")
# replace = input("На что меняем:")
# print(phrase.replace(find, replace))
# x = input()
# print(x.replace("ё", "е"))
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",

}

phrase = input("Введите фразу:")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)