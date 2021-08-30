import urllib.request
file = urllib.request.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read().decode('utf-8')
print(message)

# print("Enter your name: ", end='')
# somebody = input()
# print("Hi", somebody, "how are you today?")
