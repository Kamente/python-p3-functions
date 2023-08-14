#!/usr/bin/env python3


def greet_programmer(name):
    print (f"Hello {name}!")
greet_programmer("programmer")


def greet(name = "Justin"):
    print(f"Hello {name}!")
greet()


def greet_with_default(name="programmer"):
    print(f"Hello {name}!")
greet_with_default("Justin")
greet_with_default()


def add(num1, num2):
    print(num1 + num2)
add(5, 6)


def halve(number):
    print(number // 2)
halve(10)