"""
utils.py - Small utility functions used across my projects.
"""

import math


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    # Quick self-test
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("15 / 3 =", divide(15, 3))
    print("Area of circle with radius 5:", circle_area(5))
    print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
