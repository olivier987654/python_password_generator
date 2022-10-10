## This is a password generator script with a GUI

import random   # Import random module


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};:,./<>?|"

all = lower_case + upper_case + numbers + symbols

length = 16

password = "".join(random.sample(all, length))

print(password)

