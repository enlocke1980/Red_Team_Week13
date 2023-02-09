#!/usr/bin/env python3.7

# Python implementation here

value = int(input("Enter and integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
else:
    print(value)
    