import random

coin = ["Heads", "Tails"]
heads_in_row = 0
ten_heads_in_row = 0
for i in range(1000000):
    if random.choice(coin) == "Heads":
        heads_in_row += 1
    else:
        heads_in_row = 0
    if heads_in_row == 10:
        ten_heads_in_row += 1
        heads_in_row = 0

print("We got 10 heads in a row", ten_heads_in_row, "times.")

# totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 掷一枚11面的骰子
# for i in range(100000):
#     dice_total = random.randint(2, 12)
#     totals[dice_total] += 1

# 掷两枚6面的骰子
# for i in range(1000):
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#     dice_total = dice_1 + dice_2
#     totals[dice_total] += 1

# for i in range(2, 13):
#     print("total", i, "came up", totals[i], "times")
