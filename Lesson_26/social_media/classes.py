import requests
import random
class User:
    def __init__(self, im = "", fam = "", log = "", pas = ""):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis"
        self.rest = requests.get(url="https://api.randomdatatools.ru/").json()
        self.login = self.rest['Login'] if not log else log # !
        self.__password = self.rest["Password"] if not pas else pas
        self.name = self.rest['FirstName'] if not im else im
        self.surename = self.rest['LastName']if not fam else fam
        self.posts = [self.__lorem[random.randint(0, 5):random.randint(6,60)]]









