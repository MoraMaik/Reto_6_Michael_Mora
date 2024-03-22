def calcular_valor_prestamo(C, i, n):
    """
    Calcula el valor acumulado de un préstamo utilizando interés compuesto.
    
    Parámetros:
    C -- monto del préstamo inicial (capital)
    i -- tasa de interés mensual (en forma decimal, por ejemplo, 5% sería 0.05)
    n -- número de meses
    
    Retorna:
    El valor futuro del préstamo.
    """
    A = C * (1 + i)**n
    return A

# Solicitar al usuario que ingrese los detalles del préstamo
C = float(input('Ingrese el monto del préstamo (capital inicial): '))
i = float(input('Ingrese la tasa de interés mensual (por ejemplo, ingrese 0.05 para 5%): '))
n = int(input('Ingrese el número de meses: '))

# Calcular y mostrar el valor futuro del préstamo
valor_futuro = calcular_valor_prestamo(C, i, n)
print(f'El valor futuro del préstamo después de {n} meses es: {valor_futuro}')
