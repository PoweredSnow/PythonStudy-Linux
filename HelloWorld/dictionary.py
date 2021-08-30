phoneNumbers = {}
phoneNumbers["Jone"] = "555-1234"
# phoneNumbers = {"John": "555-1234"}
phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Bob"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"

# 按键排序
for key in sorted(phoneNumbers.keys()):
    print(key, phoneNumbers[key])
print()

# 按值排序
for value in sorted(phoneNumbers.values()):
    for key in phoneNumbers.keys():
        if phoneNumbers[key] == value:
            print(key, phoneNumbers[key])

# print(phoneNumbers)
# print(phoneNumbers["Mary"])
# print(phoneNumbers.keys())
# print(phoneNumbers.values())
# print(list(phoneNumbers.keys()))
# print(list("Hello!"))
# print(list(range(2, 5)))
