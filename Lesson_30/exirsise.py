from tkinter import *
from random import randint
#Задача 1
# win = Tk()
# Label(win,text="Логин:").grid(row = 0, column=0)
# Label(win,text="Пароль:").grid(row = 1, column=0)
# Entry(win).grid(row = 0, column=1, pady = 5)
# Entry(win).grid(row = 1, column=1,pady = 5)
# Button(win,text= "Авторизация").grid(row = 2, column=0,columnspan=2,sticky= E)
#
# win.mainloop()
# # Задача 2
# def move(e):
#     btn.place(x= randint(0,320),y= randint(0,320))
# win = Tk()
# btn = Button(win,text = "Кто нажал,\n тот красавчик", bg = "gold")
# btn.place(x=10, y=10)
# btn.bind("<Enter>", move)
#
# win.mainloop()
#Задача 3
win = Tk()

def bla():
    rb_var.set(randint(1,5))
    win.after(1000, bla)

fr = Frame()
fr.pack()
rb_var = IntVar()
rb1 = Radiobutton(fr, variable=rb_var, value= 1 )
rb1.pack(side=LEFT)

rb2 = Radiobutton(fr, variable=rb_var, value= 2)
rb2.pack(side=LEFT)

rb3 = Radiobutton(fr, variable=rb_var, value= 3)

rb3.pack(side=LEFT)
rb4 = Radiobutton(fr, variable=rb_var, value= 4)

rb4.pack(side=LEFT)
rb5 = Radiobutton(fr, variable=rb_var, value= 5)

rb5.pack(side=LEFT)

bla()



win.mainloop()