#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
result = ""

if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"

print("Last digit of {} is {} {}".format(number, last_digit, result))
