from my_module import c_to_f
import time
import random

print(random.randint(0, 100))
time.sleep(1)
print(random.random() * 10)
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = c_to_f(celsius)
print("That's %.1f degrees Fahrenheit" % fahrenheit)
