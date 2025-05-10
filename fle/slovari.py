



sl={
    "0001": "ilua",
    "0002": "masha",
    "0003": "alena"
}

print(sl.keys()) #ключи, например 0001,0002 и 0003 здесь

for i in sl.values(): #значения ключей, здесь например есть "ilua"
    print(i)

for i, f in sl.items(): #и ключи и их значения
    print(i," ",f)

sl={
    "0001": {
        "name": "ilua",
        "age": "11"
    },
    "0002": {},
    "0003": "alena"
}

print(sl["0001"]["age"])
print(sl.get("0002").get("age")) #безопасное обращения