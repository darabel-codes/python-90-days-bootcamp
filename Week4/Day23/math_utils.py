# This code is based on Python Module

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a % b