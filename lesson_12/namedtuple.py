from collections import namedtuple
citizen = namedtuple("Житель", "имя возраст статус какую_группу_ты_уважаешь")
aleх = citizen(имя = Леша,возраст = 27,статус = Предприниматель,какую_группу_ты_уважаешь = Алла Пугачева)
print(aleх.имя)
print(aleх.какую_группу_ты_уважаешь)
print(aleх)