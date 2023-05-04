
from tkinter import *
from tkinter import messagebox
# win = Tk()                    #Listbox
# def get_lst(bind_e):
#     indx = lsb.curselection()[0]
#     print(lst[indx])
# lst = ["Первый","Второй","Третье"]
# lst_tk = StringVar(value=lst)
# lsb = Listbox(win, lstvarieble=lst_tk)
# lsb.pack()
# lsb.bind("<<ListboxSelect>>",get_lst )
#
# #
# # for elem in lst:
# #     lsb.insert(END, elem)
# btn = Button(win, text= "Отправить",command= get_lst)
# btn.pack()
#
# win.mainloop()

#Labelframe
# root = Tk()
# # ===== Верхний блок =====
# frame_top = LabelFrame(root, text="Верх")
# frame_top.pack()
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()
#
# # ===== Нижний блок =====
# frame_bottom = LabelFrame(root, text="Низ")
# frame_bottom.pack()
# Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3").pack()
# Label(frame_bottom, width=7, height=4, bg='lightblue', text="4").pack()
#
#
# root.mainloop()

#message box
# root = Tk()
# messagebox.showerror("Заголовок","Одна ошибка ")
# messagebox.showinfo()
# messagebox.showwarning()
# root.mainloop()
# #pack

# root = Tk()
# f = Frame(root)
# f.pack()
# btn = Button(root, text= "Перекус ")
# # btn.pack(fill= X, expand= True)
# btn.pack(side = LEFT)
# btn1 = Button(root, text= "Перекус ")
# btn1.pack(side = LEFT)
# # btn1.pack(fill= X, expand= True)
# root.mainloop()
#
#
# root.mainloop()


# root = Tk()
# btn = Button(root, text= "Перекус ")
# btn.grid(row = 0,column=0)
#
# btn1 = Button(root, text= "Перекус1 ")
# btn1.grid(row = 0,column=1)
#
# btn2 = Button(root, text= "Перекус2 ")
# btn2.grid(row = 0,column=3)
#
# btn3 = Button(root, text= "Перекус3 ")
# btn3.grid(row = 1,column=0,columnspan=2,sticky=E)
# root.mainloop()

# root = Tk()
# btn = Button(root, text= "Перекус ")
# btn.place(x= 10,y = 300)
#
# root.mainloop()
# def color():
#     # sleep(3)
#     btn["bg"] = "green"
# from time import sleep
# def hello():
#     print("hello")
#     root.after(1000,hello)
# root = Tk()
#
# btn = Button(root, text= "К1 ")
# btn.pack()
# root.after(3000, hello)
#
# root.mainloop()
# def hello():
#     print("hello")
# root = Tk()
# btn = Button(root, text= "Что-то")
# btn.pack()
# btn.focus_set()
# btn.bind("<u>",hello)
#
# root.mainloop()
