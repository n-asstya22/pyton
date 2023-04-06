import requests
from classes import User
u1 = User(im="И", fam="Ф", log="123_nN", pas="112233")
u2 = User()
print(u1.login, u1.name, u1.surename)
print(u2.login, u2.name, u2.surename)



