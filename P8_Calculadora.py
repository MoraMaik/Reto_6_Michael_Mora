# calculadora.py

import math

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    """Calcula la mediana de una lista de números."""
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

def calcular_promedio_multiplicativo(numeros):
    """Calcula el promedio multiplicativo de una lista de números."""
    producto = math.prod(numeros)
    return producto ** (1.0 / len(numeros))

def ordenar_ascendente(numeros):
    """Ordena la lista de números de forma ascendente."""
    return sorted(numeros)

def ordenar_descendente(numeros):
    """Ordena la lista de números de forma descendente."""
    return sorted(numeros, reverse=True)

def potencia_mayor_a_menor(numeros):
    """Calcula la potencia del mayor número elevado al menor número."""
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor_numero(numeros):
    """Calcula la raíz cúbica del menor número."""
    menor = min(numeros)
    return menor ** (1.0 / 3.0)
