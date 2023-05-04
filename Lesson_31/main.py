from tkinter import *
# root = Tk()
# root.geometry("500x550")
# c = Canvas(root, width=250, height = 250, bg="lightblue" )
#
# c.pack(anchor=CENTER,expand=True)
#работа с текстом
# c.create_text(1,1,
#               text = "Пельмени " * 2,
#               anchor=NW,
#               fill= "gold")

# root.mainloop()
# ==========Прямоульник==========
# root = Tk()
# c = Canvas(root, width=250, height = 250, bg="lightblue" )
# c.pack()
# c.create_rectangle(10,10,
#                    200,150,
#                    fill="red",
#                    width=10,
#                    outline="darkred")
# root.mainloop()

# ==========Многоугольник=========
# root = Tk()
# c = Canvas(root, width=250, height = 250, bg="lightblue" )
# c.pack()
# c.create_polygon(10,10,
#                  150,150,
#                  40,40)
#
#
# root.mainloop()

# ==========Окружность===========
# root = Tk()
# c = Canvas(root, width=250, height = 250, bg="lightblue" )
# c.pack()
# c.create_oval(10,10,
#               250,150)
# root.mainloop()

# ============Ар?========
# root = Tk()
# c = Canvas(root, width=250, height=250, bg="lightblue")
# c.pack()
# # c.create_oval(10, 10,
# #               150, 150,
# #               fill="silver")
# c.create_arc(10, 10,
#              150, 150,
#              fill="red",
#              start=-45,
#              extent=30)
# c.create_arc(10, 10,
#              150, 150,
#              fill="blue",
#              start=-45,
#              extent=30,
#              style=CHORD)
# c.create_arc(10, 10,
#              150, 150,
#              fill="pink",
#              start=95,
#              extent=135,
#              style=ARC,
#              width=30)
#
# # root.mainloop()
# ============Линия========


# root = Tk()
# # c = Canvas(root, width=250, height=250, bg="lightblue")
# # c.pack()
# c.create_line(10,10,
#               150,150,
#               arrow ="first",
#               arrowshape =(50,50,50),
#               width = 20)
#
# root.mainloop()
#

# root = Tk()
# c = Canvas(root, width=250, height=250, bg="lightblue")
# c.pack()
# c.create_rectangle(10,10,
#                    200,150,
#                    fill="red",
#                    width=10,
#                    outline="darkred",
#                    dash = "-",
#                    activefill= "blue")
# root.mainloop()

#задача1
# sec= 0
root = Tk()
# def s():
#     global sec
#     c.delete("all")  # где c = Canvas()
#     sec+=1
#     c.create_image(300, 240, image=img)
#     c.create_text(300, 250,
#                   text=sec,
#                   font="Apial 25")
#     c.after(1000,s)
#     if sec == 16:
#         root.destroy()
#
#
# c = Canvas(root, width=600, height=500, bg="lightblue")
# c.pack(anchor=CENTER,expand=True)
# c.create_text(300,250,
#               text=sec,
#               font="Apial 25")
# img = PhotoImage(file="clock.png").subsample(2,2)
# c.create_image(300,240,image=img)
# s()


c = Canvas(root, width=900, height=200, bg="lightblue")
c.pack()
c.create_text(10,10,anchor= NW,text= "Школа",font = "Apial 20")
c.create_line(150,25, 250, 25,arrow = LAST )
c.create_text(300,10,anchor= NW,text= "Туда-сюда",font = "Apial 20")
c.create_line(500,25, 600, 25,arrow = LAST )
c.create_text(650,10,anchor= NW,text= "Успех!!!",font = "Apial 20")






root.mainloop()
