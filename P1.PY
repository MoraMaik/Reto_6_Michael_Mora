import math

def calcular_volumen_esfera(r1):
    """Calcula el volumen de una esfera dado su radio."""
    return (4.0/3.0) * math.pi * r1**3

def calcular_area_superficial_esfera(r1):
    """Calcula el área superficial de una esfera dado su radio."""
    return 4.0 * math.pi * r1**2

def calcular_volumen_cono(r2, h):
    """Calcula el volumen de un cono dados el radio y la altura."""
    return (1.0/3.0) * math.pi * r2**2 * h

def calcular_area_superficial_cono(r2, h):
    """Calcula el área superficial de un cono (sin la base) dados el radio y la altura."""
    s = math.sqrt(r2**2 + h**2)  # Generatriz del cono
    return math.pi * r2 * s

def saludar():
    print("Programa para calcular el volumen y el área superficial de una esfera y un cono.")

def pedir_datos():
    r1 = float(input('Ingrese el radio r1 de la esfera: '))
    r2 = float(input('Ingrese el radio r2 del cono: '))
    h = float(input('Ingrese la altura h del cono: '))
    return r1, r2, h

def main():
    saludar()
    r1, r2, h = pedir_datos()
    print(f'Volumen de la esfera: {calcular_volumen_esfera(r1)}')
    print(f'Área superficial de la esfera: {calcular_area_superficial_esfera(r1)}')
    print(f'Volumen del cono: {calcular_volumen_cono(r2, h)}')
    print(f'Área superficial del cono (sin la base): {calcular_area_superficial_cono(r2, h)}')

if __name__ == '__main__':
    main()
