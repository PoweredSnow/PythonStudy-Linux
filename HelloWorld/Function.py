def myFuction(mark):
    global price    # 强制使用全局变量
    price += 900
    mark += 100
    print()


price = 100
mark = 900
myFuction(mark)
print(price)
print(mark)
print("Done the function")
