import pickle
# a = []
# for i in range(4):
#     a.append(input())
# f = open("infor.pkl", 'wb')
f = open("infor.pkl", 'rb')
# pickle.dump(a, f)
print(pickle.load(f))
f.close()
