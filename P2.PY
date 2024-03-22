import math

def calcular_area(a, b, r):
    """Calcula el área de la figura dada."""
    area_rectangulo = a * b
    area_circulo = math.pi * r**2  # Área de un círculo completo
    return area_rectangulo + area_circulo

def calcular_perimetro(a, b, r):
    """Calcula el perímetro de la figura dada."""
    longitud_rectangulo = 2 * a
    circunferencia_circulo = 2 * math.pi * r  # Perímetro de un círculo completo
    return longitud_rectangulo + circunferencia_circulo

# Solicitar al usuario que ingrese los valores de a, b y r
a = float(input('Ingrese la longitud a del rectángulo: '))
b = float(input('Ingrese la altura b del rectángulo: '))
r = float(input('Ingrese el radio r de los semicírculos: '))

# Calcular y mostrar los resultados
print(f'Área de la figura: {calcular_area(a, b, r)}')
print(f'Perímetro de la figura: {calcular_perimetro(a, b, r)}')
