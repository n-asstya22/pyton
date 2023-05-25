


slovar = {"key1": "value1",
          "ke ng gnf jyy2": "value2",
          "hndgnhgnnr": "value3",
          "kedgh ndhgny4": "value4",
          "ghngdhnteyn": "value5"}

#values = slovar.values()    #   1
#keys = slovar.keys()

#===============
keys = []    #   2
values = []
for (key,value) in slovar.items():
    keys.append(key)
    values.append(value)
#===============
print(keys)
print(values)