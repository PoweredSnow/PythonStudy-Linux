try:
    file = open("somefile.txt", "r")
except:
    print("Couldn't open the file. Do you want to reenter the filename?")

# wordDic = {}
# while True:
#     choice = input("Add or look up a word (a/l/q)? ")
#     if choice == 'a':
#         word = input("Type the word: ")
#         definition = input("Type the definition: ")
#         wordDic[word] = definition
#         print("Word added!")
#     elif choice == 'l':
#         word = input("Type the word: ")
#         if word in wordDic:
#             print(wordDic[word])
#         else:
#             print("That word isn't in the dictionary yet.")
#     elif choice == 'q':
#         break

# import random
# import time

# list = []
# j = 0
# for i in range(5):
#     list.append(random.randint(1, 20))
# print(list)
# while j != 10:
#     print(random.random())
#     time.sleep(3)
#     j += 1

# class BankAccount:
#     def __init__(self, name, account, balance):
#         self.name = name
#         self.account = account
#         self.balance = balance

#     def printAccount(self):
#         print("Balance: %.2f" % self.balance)

#     def saveMoney(self, money):
#         self.balance = self.balance + money

#     def withdrawMoney(self, money):
#         self.balance = self.balance - money


# class InterestAccount(BankAccount):
#     def __init__(self, name, account, balance, interestRate):
#         BankAccount.__init__(self, name, account, balance)
#         self.interestRate = interestRate

#     def addInterest(self, time):
#         for i in range(time):
#             self.balance = self.balance + self.balance * self.interestRate


# myAccount = InterestAccount("neri", "12345678", 1000, 0.1)
# myAccount.printAccount()
# myAccount.addInterest(3)
# myAccount.printAccount()

# name = []
# print("Enter 5 names:")
# for i in range(5):
#     name.append(input())
# print("The names are ", end='')
# for i in range(5):
#     print("%s " % name[i], end='')
# print()
# num = int(input("Replace one name. Which one? (1-5): "))
# del name[num - 1]
# name.insert(num - 1, input("New name: "))
# print("The names are ", end='')
# for i in range(5):
#     print("%s " % name[i], end='')
# print()


# import time
# num = int(input("How many seconds do you want? "))
# for i in range(num, 0, -1):
#     print(i, end='')
#     for j in range(i, 0, -1):
#         print(" *", end='')
#     time.sleep(1)
#     print()
# print("BLAST OFF!")

# input0 = int(input("Which multiplication table would you like?\n"))
# input1 = int(input("How high do you want to go?\n"))
# print("Here's your table:")
# i = 0
# while i != input1 + 1:
#     print("%d x %d = %d" % (input0, i, input0 * i))
#     i += 1

# import easygui

# name = easyguiti.enterbox("What's your name?")
# roomnum = int(easygui.enterbox("What's your roomnumber?"))
# street = easygui.enterbox("Which street do you live on?")
# city = easygui.enterbox("Where do you come from?")
# postCode = int(easygui.enterbox("What's the post nummber of your city?"))
# easygui.msgbox("%s\n%d %s\n%s\n%d" % (name, roomnum, street, city, postCode))

# print(input() + input())

# f = float(input("input:"))
# if (f - int(f)) >= 0.5:
#     print(int(f + 1))
# else:
#     print(int(f))

# F = easygui.integerbox()
# C = 5/9*(F-32)
# easygui.msgbox("%d" % C)
