capitals ={"USA":"Washington D.C",
           "INDIA" : "NEW DELHI",
           "CHINA":"BEIJING",
           "RUSSIA":"MOSCOW"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("JAPAN"))

if capitals.get("RUSSIA"):
    print("that capital exists")
else:
    print("that capital dosen't exists")

capitals.update({"germany":"berlin"})
capitals.update({"USA":"DETROIT"})
capitals.pop("CHINA")
capitals.popitem()
capitals.clear()

keys=capitals.keys()

for key in capitals.keys():
    print(key)

values=capitals.values()
for value in capitals.values():
    print(value)

items=capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")