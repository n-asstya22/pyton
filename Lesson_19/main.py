import easygui
def atbash(text):
    a= "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    a2 = a[::-1]
    f_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    f_a2 = f_a[::-1]

    b = ""
    for letter in text:
        if letter not in a and letter not in f_a2:
            b += letter
        elif letter in a:
            i = a.index(letter)
            i2 = a2[i]
            b = b + i2
        else:
            i = f_a.index(letter)
            i2 = f_a2[i]
            b = b + i2

    easygui.msgbox(
            msg= b
             )
#    print(b)
msg = easygui.enterbox(
    msg="Введите текст:"
).upper()


# msg = input("Введите сообщение:").upper()
atbash(msg)
