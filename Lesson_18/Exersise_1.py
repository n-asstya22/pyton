#Задача_1
import easygui
import random

def rock_paper_scissors():
    otvets = {'Paper':'img/Paper.png',
              'rock':'img/rock.png',
              'scissors':'img/scissors.png' }

    result = easygui.buttonbox(

        msg= 'Выбери фгуру',
        title= 'Камень, ножницы, бумага',
        images = ['img/Paper.png','img/rock.png','img/scissors.png'],
        choices=('выход',) )
    print(otvets.keys())
    comp = random.choice(list(otvets.keys()))
    print(comp)
    if result == otvets['rock'] and comp == 'scissors':
        easygui.msgbox(msg="Урааааа 🦑")
    if result == otvets['Paper'] and comp == 'rock':
        easygui.msgbox(msg="Урааааа 🦑")
    if result == otvets['Paper'] and comp == 'rock':
        easygui.msgbox(msg="Урааааа 🦑")




def guess_the_number():
    n = easygui.integerbox(msg='Какое число?',
                           lowerbound=1,
                           upperbound=99)
    n_c = random.randint(1, 99)
    if n == n_c:
        return  # выход из функции

    while n != n_c:
        if n > n_c:
            n = easygui.integerbox(msg='Какое число?',
                                   lowerbound=1,
                                   upperbound=99,
                                   image='img/МЕНЬШЕ.png')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()