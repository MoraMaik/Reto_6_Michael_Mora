def calcular_contagiados(C, D):
    """
    Calcula el número total de personas contagiadas de Covid-19 después de D días.
    
    Parámetros:
    C -- número actual de contagiados
    D -- número de días después de hoy
    
    Retorna:
    El número total de personas contagiadas después de D días.
    """
    C_total = C * (2 ** D)
    return C_total

# Solicitar inGresar el número actual de contagiados y el número de días
C = int(input('Ingrese el número actual de contagiados de Covid-19: '))
D = int(input('Ingrese el número de días a partir de hoy: '))

# Calcular y mostrar el número total de contagiados después de D días
total_contagiados = calcular_contagiados(C, D)
print(f'El número total de personas que se han contagiado después de {D} días es: {total_contagiados}')
