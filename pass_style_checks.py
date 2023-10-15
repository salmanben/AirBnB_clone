#!/usr/bin/python3
"""This module defines a func pass pycodestyle checks."""


def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}! How are you today?")


user_name = input("Enter your name: ")
greet(user_name)
