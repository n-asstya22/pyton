import tkinter as tk
def knopka(event):
    print("привет")
window = tk.Tk()  #начало
window.geometry("500x400")
window.title("Окно")
bt = tk.Button(window, text = "Кнопка")  #сщздание кнопки
bt.pack()  #размещение кнопки
bt["text"] = "Привет"  #изменение конфигурации
bt["font"] =("Times new Roman",
             15,
             "bold" #жирный
             # "underline" # подчеркнутое
             # "italic" # курсив
             # "overstrike" # зачеркнутая
             )
bt["background"] = "gold4"  #цвет фона
# bt["Bg"] = "gold4"
bt["foreground"] = "pink2"  # фвет текста
# bt["fd"] = "pink2"  # фвет текста
bt["width"] = 10
bt["height"] = 3
bt["borderwidth"] = 10
# bt["commend"] = knopka # нажатие на левую кнопку мыжи
bt.bind("<Double-Button-1>",knopka)








window.mainloop()  #конец
