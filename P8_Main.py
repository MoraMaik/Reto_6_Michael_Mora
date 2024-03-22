# main.py

from P8_Calculadora import (calcular_promedio, calcular_mediana, 
                        calcular_promedio_multiplicativo, ordenar_ascendente, 
                        ordenar_descendente, potencia_mayor_a_menor, 
                        raiz_cubica_menor_numero)

# Pedir al usuario que ingrese 5 números reales
numeros = []
for _ in range(5):
    numero = float(input("Ingrese un número real: "))
    numeros.append(numero)

# Realizar los cálculos y mostrar los resultados
print(f"Promedio: {calcular_promedio(numeros)}")
print(f"Mediana: {calcular_mediana(numeros)}")
print(f"Promedio multiplicativo: {calcular_promedio_multiplicativo(numeros)}")
print(f"Números ordenados de forma ascendente: {ordenar_ascendente(numeros)}")
print(f"Números ordenados de forma descendente: {ordenar_descendente(numeros)}")
print(f"Potencia del mayor número elevado al menor número: {potencia_mayor_a_menor(numeros)}")
print(f"Raíz cúbica del menor número: {raiz_cubica_menor_numero(numeros)}")
