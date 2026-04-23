"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

try:
    if len(sys.argv) != 3:
        raise ValueError


    total_load = float(sys.argv[1]) 
    num_supports = int(sys.argv[2])
    if num_supports == 0:
        raise ValueError   
     
    load_per_support = total_load / num_supports  

    print(f"Carga por punto de soporte: {load_per_support:.2f} N")


except ValueError:
    print("Error: input invalido! introduzca solo valores numericos")
          
except ZeroDivisionError:
    print("Error: ¡ No se puede dividir por cero! El numero de puntos de soporte debe ser mayor que cero.")

