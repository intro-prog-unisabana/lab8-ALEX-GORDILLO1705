"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

try:
    if len(sys.argv) != 3:
        raise ValueError

    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])

    if num_supports == 0:
        raise ZeroDivisionError

    result = total_load / num_supports
    print(f"Load per support point: {result:.2f} N")

except ValueError:
    print("Error: Invalid input! Enter numeric values only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")