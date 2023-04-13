import tkinter as tk
# def Knopka(event):
#     message = ent.get()
#     ent.delete(0, "end")
#     lab["text"] = message
#     print(message)
#
#     message2 = txt.get(1.0,"end")
#     txt.delete(0.0, "end")
#     print(message2)
#
#
# window = tk.Tk()  #начало
# window.geometry("300x400")
# lab = tk.Label(window, text ="Бубики",width =70)
# lab.pack()
# lab["background"] = "purple"
# lab["foreground"] = "gold"
# ent = tk.Entry(bd =7, width = 10)
# ent.pack()
#
#
# bt = tk.Button(window)
# bt.pack()
# bt["text"] = "Oтправить"
# bt["background"] = "purple"
# bt["foreground"] = "gold"
# bt.bind("<Button-1>",Knopka)
# txt = tk.Text(window, width = 20, height =  5 )
# txt.pack()
#
#
# window.mainloop()

# def Knopka(event):
#     message = ent.get()
#     ent.delete(0, "end")
#     lab["text"] = message
#     print("Адрес:",message)
#
#     message2 = txt.get(1.0,"end")
#     txt.delete(0.0, "end")
#     print("Комментарий:",message2)
#
# window = tk.Tk()
# window.geometry("375x450")
# window.configure(background='wheat')
#
# lab = tk.Label(window, text ="Ваш адрес",width =70,font ="bold")
# lab["background"] = "wheat"
# lab.pack()
#
# ent = tk.Entry(bd =7, width = 25)
# ent.pack()
#
# lab = tk.Label(window, text ="Комментарий",width =70,font ="bold")
# lab["background"] = "wheat"
# lab.pack()
#
# txt = tk.Text(window, width = 25, height = 7 )
# txt.pack()
#
# bt = tk.Button(window)
# bt.pack()
# bt["text"] = "Oтправить"
# bt["background"] = "blue"
# bt["width"] = 10
# bt["height"] = 1
# bt.bind("<Button-1>",Knopka)
#
# window.mainloop()

def Knopka(event):
    print(bt["background"])
    if bt["background"] == "red":
        lab["text"] = "Красный"
    elif bt["background"] == "oradge":
        lab["text"] = "Оранжевый"
    elif bt["background"] == "yellow":
        lab["text"] = "Желтый"
    elif bt["background"] == "green":
        lab["text"] = "Зеленый"
    elif bt["background"] == "lightblue":
        lab["text"] = "Голубой"
    elif bt["background"] == "blue":
        lab["text"] = "Синий"
    else:
        lab["text"] = "Фиолетовый"


window = tk.Tk()
window.geometry("300x450")

lab = tk.Label(window, text ="",width =70,font ="bold")

lab.pack()

bt = tk.Button(window)
bt.pack()
bt["background"] = "red"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "orange"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "yellow"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "green"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "lightblue"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "blue"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)

bt = tk.Button(window)
bt.pack()
bt["background"] = "purple"
bt["width"] = 300
bt["height"] = 2
bt.bind("<Button-1>",Knopka)




window.mainloop()



