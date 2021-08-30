import time

print("---EXAMPLE : Loading 效果---")

print("Loading", end='')
for i in range(20):
    print(".", end='', flush=True)
    time.sleep(0.5)
print()
