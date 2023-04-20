import tkinter as tk
#
# def cheak():      #Checkbutton
#     print(var.get())
#
# root = tk.Tk()
# var = tk.BooleanVar()
# ch = tk.Checkbutton(root,
#                     text="Подписка",
#                     variable=var,   #значение в переменную
#                     onvalue=True,
#                     offvalue=False,
#                     command=cheak
#                     )

#------------------------------------------
# root = tk.Tk()        #Radiobutton
# var = tk.IntVar()
#
# def cheak():
#     print(var.get())
#
# rb = tk.Radiobutton(root,
#                     text="кнопка",
#                     variable=var,
#                     value= 1,
#                     command= cheak)
# rb.pack()
# rb1 = tk.Radiobutton(root,
#                     text="кнопка",
#                     variable=var,
#                     value= 2,
#                     command= cheak)
# rb1.pack()
#
# root = tk.Tk()
#------------------------------------------
# root = tk.Tk()        #Scale
# root.geometry('300x400')
#
# def g(b):
#     print(sk.get()) #получить значение
#     print(b)
# sk = tk.Scale(root,
#               from_=500,
#               to=1000,
#               width=50,
#               length=500,
#               orient=tk.HORIZONTAL,
#               tickinterval=100, #шаг
#               resolution=50,
#               command=g)
#
# sk.pack()
# root.mainloop()


# root = tk.Tk()
# img = tk.PhotoImage(file="39dc0d67814f328bb4f4f5451f3d075b.png")
#
#
# root.mainloop()
# def switch():
#     if bt1['state'] == "disabled":
#         bt1['state'] = "normal"
#     else:
#         bt2['state'] = "disabled"
#
#
#
#
# root = tk.Tk()
# bt1 = tk.Button(root,
#                text="активиновать",
#                state=tk.DISABLED,
#                fg='red',
#                disabledforeground="grey",
#                width= 30)
#
# bt1.pack(pady=20, ipady=20)
#
# bt2 = tk.Button(root,
#                text="активиновать2",
#                width= 30,
#                command=switch)
# bt2.pack(pady=20, ipady=20)
# root.mainloop()
#
# #ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ ENTRY
# ent = tk.Entry(root)
# ent.pack()
# ent.insert(tk.END= , "ативировать"

# def act():
#     if b["state"] == "disabled":
#         b["state"] = "normal"
#         b["text"] = "Активен"
#     else:
#         b["state"] = "disabled"
#         b['text'] = "Не активен!"
#
#
#
# root = tk.Tk()
#
# cb = tk.Checkbutton(root,
#                     text="Активировать",
#                     command=act)
# # cb.select()
# cb.pack()
# b = tk.Button(root,
#               text="Не активен!",
#               state=tk.DISABLED)
# b.pack()
#
# root.mainloop()

root = tk.Tk()
def bold():
    if cb1_val.get():  # если св1 == True
        lab["font"] += " bold"
    else:
        lab["font"] = lab["font"].replace(" bold", "")


def italic():
    if cb2_val.get():  # если св1 == True
        lab["font"] += " italic"
    else:
        lab["font"] = lab["font"].replace(" italic", "")


def overs():
    if cb3_val.get():  # если св1 == True
        lab["font"] += " overstrike"
    else:
        lab["font"] = lab["font"].replace(" overstrike", "")


def und():
    if cb4_val.get():  # если св1 == True
        lab["font"] += " underline"
    else:
        lab["font"] = lab["font"].replace(" underline", "")


lab = tk.Label(root,
               text="abc",
               font="Arial 12")
lab.pack()
# =========
cb1_val = tk.BooleanVar()
cb1 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=bold
                     )
cb1.pack()
# =========
cb2_val = tk.BooleanVar()
cb2 = tk.Checkbutton(root,
                     text="Курсив",
                     variable=cb2_val,
                     onvalue=True,
                     offvalue=False,
                     command=italic
                     )
cb2.pack()
# =========
cb3_val = tk.BooleanVar()
cb3 = tk.Checkbutton(root,
                     text="Зачеркнутый",
                     variable=cb3_val,
                     onvalue=True,
                     offvalue=False,
                     command=overs
                     )
cb3.pack()
# =========
cb4_val = tk.BooleanVar()
cb4 = tk.Checkbutton(root,
                     text="Подчеркнутый",
                     variable=cb4_val,
                     onvalue=True,
                     offvalue=False,
                     command=und
                     )
cb4.pack()

root.mainloop()