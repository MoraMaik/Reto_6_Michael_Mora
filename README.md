# Reto_6_Michael_Mora

Como primera parte se desarrolla los ejercicos de la [clase 9](http://https://github.com/fegonzalez7/pdc_unal_clase9 "clase 9") .

**E1**: realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.

```python
# Constante de gravitación universal
G = 6.67430e-11  # en N(m/kg)^2

def calcular_fuerza_gravedad(m1, m2, r):
    """
    Calcula la fuerza de gravedad entre dos masas dadas a una distancia.
    
    Parámetros:
    m1 -- masa del primer objeto (kg)
    m2 -- masa del segundo objeto (kg)
    r -- distancia entre los centros de las dos masas (m)
    
    Retorna:
    Fuerza de gravedad en Newtons
    """
    F = G * m1 * m2 / r**2
    return F

# Solicitar al usuario que ingrese las masas y la distancia
masa1 = float(input('Ingrese la masa del primer objeto (en kg): '))
masa2 = float(input('Ingrese la masa del segundo objeto (en kg): '))
distancia = float(input('Ingrese la distancia entre los centros de las dos masas (en m): '))

# Calcular la fuerza de gravedad
fuerza = calcular_fuerza_gravedad(masa1, masa2, distancia)

# Mostrar el resultado
print(f'La fuerza de gravedad entre las masas es: {fuerza} N')

```
*Imporatante:* Este código pedirá al usuario que introduzca los valores directamente en el notebook sin necesidad de interfaces gráficas adicionales

**E2**:  Uno de los módulos que trae python es math, hacer un porgrama en Python importando math y usar 5 de las funciones incluidas en este módulo.


```python
import math

def saludar():
    """Imprime un saludo."""
    print("¡Hola Profe! Aqui puedes mirar la aplicacion del ejercicio.")

def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo."""
    return ancho * alto

def elevar_cuadrado(numero):
    """Eleva un número al cuadrado utilizando math.pow."""
    return math.pow(numero, 2)

def sumar_dos_numeros(num1, num2):
    """Suma dos números."""
    return num1 + num2

def main():
    """Función principal del programa."""
    saludar()
    
    # Calcular el área de un rectángulo
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    alto = float(input("Ingrese el alto del rectángulo: "))
    area = calcular_area_rectangulo(ancho, alto)
    print(f"El área del rectángulo es: {area}")

    # Elevar un número al cuadrado
    numero = float(input("Ingrese un número para elevar al cuadrado: "))
    cuadrado = elevar_cuadrado(numero)
    print(f"El cuadrado del número es: {cuadrado}")

    # Sumar dos números
    num1 = float(input("Ingrese el primer número para sumar: "))
    num2 = float(input("Ingrese el segundo número para sumar: "))
    suma = sumar_dos_numeros(num1, num2)
    print(f"La suma de los dos números es: {suma}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

```
*Importante*: Este programa hace:

+ Al ejecutar la función main, primero se mostrará un saludo al usuario.
+ Luego, se le pedirá que ingrese las dimensiones de un rectángulo y calculará su área.
+ Después, se le pedirá que ingrese un número para elevarlo al cuadrado.
+ Por último, se le pedirá que ingrese dos números para sumarlos.
______________________
Continuamos con el desarrollo del reto.

## **Punto 1**:
Para este punto buscamos implementar funciones ya dadas en clase, ademas de tener en cuenta algunas formulas particulares, como:

#### Fórmulas matemáticas

- **Volumen de una esfera**  
  El volumen `V` de una esfera se calcula con la fórmula:  
  `V_esfera = 4/3 * π * r³`

- **Área superficial de una esfera**  
  El área superficial `A` de una esfera se calcula con la fórmula:  
  `A_esfera = 4 * π * r²`

- **Volumen de un cono**  
  El volumen `V` de un cono se calcula con la fórmula:  
  `V_cono = 1/3 * π * r² * h`

- **Área superficial de un cono (sin la base)**  
  El área superficial `A` de un cono se calcula con la fórmula del área lateral:  
  `A_cono = π * r * ℓ`  
  donde `ℓ` es la generatriz del cono, que se puede calcular con el teorema de Pitágoras si no se da directamente:  
  `ℓ = √(r² + h²)`

```python
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

```

Este código define las siguientes funciones:

+ calcular_volumen_esfera: Calcula el volumen de una esfera dado su radio r1.
+ calcular_area_superficial_esfera: Calcula el área superficial de una esfera dado su radio r1.
+ calcular_volumen_cono: Calcula el volumen de un cono dados su radio r2 y altura h.
+ calcular_area_superficial_cono: Calcula el área superficial del cono sin contar la base, utilizando la generatriz que se calcula con la fórmula de la hipotenusa de un triángulo rectángulo.
+ saludar: Imprime un mensaje de saludo al usuario.
+ pedir_datos: Solicita al usuario ingresar los valores necesarios y los retorna.
+ main: Función principal que ejecuta el programa.

Al ejecutar el programa, se saludará al usuario y se le pedirá que ingrese los radios y la altura para calcular y mostrar los volúmenes y áreas superficiales correspondientes.

______________________
## **Punto 2**:

[![p2.jpg](https://i.postimg.cc/wv7bV32p/p2.jpg)](https://postimg.cc/62x06WFj)

Vamos a definir dos funciones: una para calcular el área y otra para calcular el perímetro de esta figura.

La función matemática para el área de esta figura será la suma del área del rectángulo (a * b) y el área de un círculo completo (π * r^2), ya que dos semicírculos forman un círculo.

Para el perímetro, sumaremos la longitud del rectángulo (2 * a) y la circunferencia de un círculo completo (2 * π * r), ya que el perímetro incluirá dos semicírculos que juntos forman una circunferencia completa.

```python
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

```
______________________
## **Punto 3**:

```python
def calcular_peso_total_aves(N, M, K):
    """
    Calcula el peso total de las aves dado el número de gallinas, gallos y pollitos.
    
    Parámetros:
    N -- número de gallinas
    M -- número de gallos
    K -- número de pollitos
    
    Retorna:
    Peso total en kilos
    """
    peso_gallina = 6  # cada gallina pesa 6 kilos
    peso_gallo = 7    # cada gallo pesa 7 kilos
    peso_pollito = 1  # cada pollito pesa 1 kilo
    
    peso_total = (N * peso_gallina) + (M * peso_gallo) + (K * peso_pollito)
    return peso_total

# Ejemplo de uso:
N = int(input('Ingrese el número de gallinas: '))
M = int(input('Ingrese el número de gallos: '))
K = int(input('Ingrese el número de pollitos: '))

print(f'El peso total de las aves es: {calcular_peso_total_aves(N, M, K)} kilos')

```

Cuando llamamos a la función calcular_peso_total_aves, debes pasarle los valores de N, M y K que corresponden al número de gallinas, gallos y pollitos, respectivamente. La función luego devuelve el peso total de las aves.

______________________
## **Punto 4**:

```python
def calcular_cambio(P, M, H, B):
    """
    Calcula el cambio o lo que queda debiendo después de comprar panes, leche y huevos.
    
    Parámetros:
    P -- número de panes
    M -- número de bolsas de leche
    H -- número de huevos
    B -- valor del billete con el que se paga
    
    Retorna:
    Un mensaje indicando el cambio o lo que queda debiendo.
    """
    precio_pan = 300
    precio_leche = 3300
    precio_huevo = 350
    
    total_panes = P * precio_pan
    total_leche = M * precio_leche
    total_huevos = H * precio_huevo
    
    total_compra = total_panes + total_leche + total_huevos
    cambio = B - total_compra
    
    if cambio < 0:
        return f'Quedas debiendo {abs(cambio)} pesos.'
    else:
        return f'Tu cambio es {cambio} pesos.'

# Solicitar al usuario que ingrese las cantidades y el billete con el que va a pagar
P = int(input('Ingrese el número de panes a comprar: '))
M = int(input('Ingrese el número de bolsas de leche a comprar: '))
H = int(input('Ingrese el número de huevos a comprar: '))
B = int(input('Ingrese el valor del billete con el que va a pagar: '))

# Llamar a la función y mostrar el resultado
print(calcular_cambio(P, M, H, B))

```

Este código solicitará al usuario los valores de P, M, H, y B y luego calculará el cambio o lo que queda debiendo después de realizar la compra. Finalmente, mostrará un mensaje con el resultado.

______________________
## **Punto 5**:



