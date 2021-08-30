import time
import datetime
import random

messages = [
    "Of all the trees we could've hit, we had to get one that hits back.",
    "If he doesn't stop trying to save your life he's going to kill you.",
    "It is our choices that show what we truly are, far more than our abilities.",
    "I am a wizard, not a baboon brandishing a stick.",
    "Greatness inspires envy, envy engenders spite, spite spawns lies.",
    "In dreams, we enter a world that's entirely our own.",
    "It is my belief that the truth is generally preferable to lies.",
    "Dawn seemed to follow midnight with indent haste."
]

print("Typing speed test. Type the following message.I will time tou.")
time.sleep(2)
print("\nReady...")
time.sleep(1)
print("\nSet...")
time.sleep(1)
print("\nGo:")
message = random.choice((messages))
print("\n " + message)
start_time = datetime.datetime.now()    # 启动时钟
typing = input('>')
end_time = datetime.datetime.now()      # 停止时钟
# 计算经过的时间
diff = end_time - start_time
typing_time = diff.seconds + diff.microseconds / 1000000
cps = len(message) / typing_time
wpm = cps * 60 / 5
print(f"\nYou typed {len(message)} characters in {typing_time:.2f} seconds.")
print(f"That's {cps:.2f} chars per sec, or {wpm:.2f} words per minute.")
if typing == message:
    print("You don't make any mistakes.")
else:
    print("But, you made at least one mistake.")
