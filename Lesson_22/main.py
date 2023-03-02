import json
# wr_f = open("file.json","w", encoding="utf-8")
# #wr_f.write("True")
# cotnent = [None, True, (1, 2, 3), [1, 2, 3],"hello", "привет"]
# json.dump(cotnent, wr_f, ensure_ascii=False)
# json.dumps() #не записывает в файл
# wr_f.close()
# # r_f = open("file.json", "r", encoding="utf-8")
# # # print(r_f.read())
# # print(json.load(r_f))
# #
# # r_f.close()

#Задача1
# r_f = open("file.txt", "r", encoding="utf-8")
# content = r_f.readlines()
# d = {}
# for i in content:
#     splited = i.split(": ")
#     d[splited[0]] = splited[1].rstrip()
# print(d)
# r_f.close()
# f = open("file.json","w", encoding="utf-8")
# json.dump(d, f, ensure_ascii=False)
import requests
respones = requests.get(url="http://api.open-notify.org/iss-now.json")
data = (respones.json()["iss_position"])
print(f"Широта:{data['latitude']},Долгота:{data['longitude']}")