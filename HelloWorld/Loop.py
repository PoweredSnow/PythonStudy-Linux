# 列出热狗各部分的卡路里
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print("\tDog \tBun \tKetchup\tMustard\tOnions\tCalories")  # 打印表头
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (bun * bun_cal) + (dog * dog_cal) + \
                        (ketchup * ket_cal) + (mustard * mus_cal) + \
                        (onion * onion_cal)
                    print("# %d \t %d \t %d \t %d \t %d \t %d \t %d" %
                          (count, dog, bun, ketchup, mustard, onion, total_cal))
                    count += 1

# numBlocks = int(input('How many blocks of stars do you want? '))
# for block in range(1, numBlocks + 1):
#     print("block = %d" % block)
#     for line in range(1, block * 2):
#         for star in range(1, (block + line) * 2):
#             print("*", end='')
#         print('    line = %d\tstar = %d' % (line, star))
#     print()

# for multiplier in range(5, 8):
#     for i in range(1, 11):
#         print("%d x %d = %d" % (i, multiplier, i * multiplier))
#     print()

# for i in range(1, 6):
#     print()
#     print('i =', i, 'Hello, how ', end='')
#     if i == 3:
#         break
#     print('are you today?')

# print("Type 3 to continue, anything else to quit.")
# someInput = input()
# while someInput == '3':
#     print("Thank you for the 3. Very kind of you.")
#     print("Type 3 to continue, anything else to quit.")
#     someInput = input()
# print("That's not 3, so I'm quitting now.")

# for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
#     print(cool_guy, "is the coolest guy ever!")
