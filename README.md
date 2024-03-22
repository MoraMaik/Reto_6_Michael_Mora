# Reto_6_Michael_Mora

Como primera parte se desarrolla los ejercicos de la [clase 9](http://https://github.com/fegonzalez7/pdc_unal_clase9 "clase 9") .

**E1**: realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una funcion.

```python
# Constante de gravitacion universal
G = 6.67430e-11  # en N(m/kg)^2

def calcular_fuerza_gravedad(m1, m2, r):
    """
    Calcula la fuerza de gravedad entre dos masas dadas a una distancia.
    
    Parametros:
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
*Imporatante:* Este codigo pedira al usuario que introduzca los valores directamente en el notebook sin necesidad de interfaces graficas adicionales

**E2**:  uno de los modulos que trae python es math, hacer un porgrama en Python importando math y usar 5 de las funciones incluidas en este modulo.


```python
import math

def saludar():
    """Imprime un saludo."""
    print("¡Hola Profe! Aqui puedes mirar la aplicacion del ejercicio.")

def calcular_area_rectangulo(ancho, alto):
    """Calcula el area de un rectangulo."""
    return ancho * alto

def elevar_cuadrado(numero):
    """Eleva un numero al cuadrado utilizando math.pow."""
    return math.pow(numero, 2)

def sumar_dos_numeros(num1, num2):
    """Suma dos numeros."""
    return num1 + num2

def main():
    """Funcion principal del programa."""
    saludar()
    
    # Calcular el area de un rectangulo
    ancho = float(input("Ingrese el ancho del rectangulo: "))
    alto = float(input("Ingrese el alto del rectangulo: "))
    area = calcular_area_rectangulo(ancho, alto)
    print(f"El area del rectangulo es: {area}")

    # Elevar un numero al cuadrado
    numero = float(input("Ingrese un numero para elevar al cuadrado: "))
    cuadrado = elevar_cuadrado(numero)
    print(f"El cuadrado del numero es: {cuadrado}")

    # Sumar dos numeros
    num1 = float(input("Ingrese el primer numero para sumar: "))
    num2 = float(input("Ingrese el segundo numero para sumar: "))
    suma = sumar_dos_numeros(num1, num2)
    print(f"La suma de los dos numeros es: {suma}")

# Ejecutar la funcion principal
if __name__ == "__main__":
    main()

```
*Importante*: Este programa hace:

+ Al ejecutar la funcion main, primero se mostrara un saludo al usuario.
+ Luego, se le pedir que ingrese las dimensiones de un rectangulo y calculara su area.
+ Despues, se le pedira que ingrese un numero para elevarlo al cuadrado.
+ Por ultimo, se le pedira que ingrese dos numeros para sumarlos.
______________________
Continuamos con el desarrollo del reto.

## **Punto 1**:
Para este punto buscamos implementar funciones ya dadas en clase, ademas de tener en cuenta algunas formulas particulares, como:

#### Formulas matematicas  

- **Volumen de una esfera**  
  El volumen `V` de una esfera se calcula con la formula:  
  `V_esfera = 4/3 * π * r³`

- **area superficial de una esfera**  
  El area superficial `A` de una esfera se calcula con la formula:  
  `A_esfera = 4 * π * r²`

- **Volumen de un cono**  
  El volumen `V` de un cono se calcula con la formula:  
  `V_cono = 1/3 * π * r² * h`

- **area superficial de un cono (sin la base)**  
  El area superficial `A` de un cono se calcula con la formula del area lateral:  
  `A_cono = π * r * ℓ`  
  donde `ℓ` es la generatriz del cono, que se puede calcular con el teorema de Pitagoras si no se da directamente:  
  `ℓ = √(r² + h²)`

```python
import math

def calcular_volumen_esfera(r1):
    """Calcula el volumen de una esfera dado su radio."""
    return (4.0/3.0) * math.pi * r1**3

def calcular_area_superficial_esfera(r1):
    """Calcula el area superficial de una esfera dado su radio."""
    return 4.0 * math.pi * r1**2

def calcular_volumen_cono(r2, h):
    """Calcula el volumen de un cono dados el radio y la altura."""
    return (1.0/3.0) * math.pi * r2**2 * h

def calcular_area_superficial_cono(r2, h):
    """Calcula el area superficial de un cono (sin la base) dados el radio y la altura."""
    s = math.sqrt(r2**2 + h**2)  # Generatriz del cono
    return math.pi * r2 * s

def saludar():
    print("Programa para calcular el volumen y el area superficial de una esfera y un cono.")

def pedir_datos():
    r1 = float(input('Ingrese el radio r1 de la esfera: '))
    r2 = float(input('Ingrese el radio r2 del cono: '))
    h = float(input('Ingrese la altura h del cono: '))
    return r1, r2, h

def main():
    saludar()
    r1, r2, h = pedir_datos()
    print(f'Volumen de la esfera: {calcular_volumen_esfera(r1)}')
    print(f'area superficial de la esfera: {calcular_area_superficial_esfera(r1)}')
    print(f'Volumen del cono: {calcular_volumen_cono(r2, h)}')
    print(f'area superficial del cono (sin la base): {calcular_area_superficial_cono(r2, h)}')

if __name__ == '__main__':
    main()

```

Este codigo define las siguientes funciones:

+ *calcular_volumen_esfera*: Calcula el volumen de una esfera dado su radio r1.
+ *calcular_area_superficial_esfera*: Calcula el area superficial de una esfera dado su radio r1.
+ *calcular_volumen_cono*: Calcula el volumen de un cono dados su radio r2 y altura h.
+ *calcular_area_superficial_cono*: Calcula el area superficial del cono sin contar la base, utilizando la generatriz que se calcula con la formula de la hipotenusa de un triangulo rectangulo.
+ *saludar*: Imprime un mensaje de saludo al usuario.
+ *pedir_datos*: Solicita al usuario ingresar los valores necesarios y los retorna.
+ *main*: Funcion principal que ejecuta el programa.

Al ejecutar el programa, se saludara al usuario y se le pedira que ingrese los radios y la altura para calcular y mostrar los volumenes y areas superficiales correspondientes.

______________________
## **Punto 2**:

[![p2.jpg](https://i.postimg.cc/wv7bV32p/p2.jpg)](https://postimg.cc/62x06WFj)

Vamos a definir dos funciones: una para calcular el area y otra para calcular el perimetro de esta figura.

La funcion matematica para el area de esta figura sera la suma del area del rectangulo (a * b) y el area de un circulo completo (π * r^2), ya que dos semicirculos forman un circulo.

Para el perimetro, sumaremos la longitud del rectangulo (2 * a) y la circunferencia de un circulo completo (2 * π * r), ya que el perimetro incluira dos semicirculos que juntos forman una circunferencia completa.

```python
import math

def calcular_area(a, b, r):
    """Calcula el area de la figura dada."""
    area_rectangulo = a * b
    area_circulo = math.pi * r**2  # area de un circulo completo
    return area_rectangulo + area_circulo

def calcular_perimetro(a, b, r):
    """Calcula el perimetro de la figura dada."""
    longitud_rectangulo = 2 * a
    circunferencia_circulo = 2 * math.pi * r  # Perimetro de un circulo completo
    return longitud_rectangulo + circunferencia_circulo

# Solicitar al usuario que ingrese los valores de a, b y r
a = float(input('Ingrese la longitud a del rectangulo: '))
b = float(input('Ingrese la altura b del rectangulo: '))
r = float(input('Ingrese el radio r de los semicirculos: '))

# Calcular y mostrar los resultados
print(f'area de la figura: {calcular_area(a, b, r)}')
print(f'Perimetro de la figura: {calcular_perimetro(a, b, r)}')

```
______________________
## **Punto 3**:

Diseñe una funcin que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def calcular_peso_total_aves(N, M, K):
    """
    Calcula el peso total de las aves dado el numero de gallinas, gallos y pollitos.
    
    Parametros:
    N -- numero de gallinas
    M -- numero de gallos
    K -- numero de pollitos
    
    Retorna:
    Peso total en kilos
    """
    peso_gallina = 6  # cada gallina pesa 6 kilos
    peso_gallo = 7    # cada gallo pesa 7 kilos
    peso_pollito = 1  # cada pollito pesa 1 kilo
    
    peso_total = (N * peso_gallina) + (M * peso_gallo) + (K * peso_pollito)
    return peso_total

# Ejemplo de uso:
N = int(input('Ingrese el numero de gallinas: '))
M = int(input('Ingrese el numero de gallos: '))
K = int(input('Ingrese el numero de pollitos: '))

print(f'El peso total de las aves es: {calcular_peso_total_aves(N, M, K)} kilos')

```

Cuando llamamos a la funcion *calcular_peso_total_aves*, debes pasarle los valores de N, M y K que corresponden al numero de gallinas, gallos y pollitos, respectivamente. La funcion luego devuelve el peso total de las aves.

______________________
## **Punto 4**:

Mi mamaa me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
def calcular_cambio(P, M, H, B):
    """
    Calcula el cambio o lo que queda debiendo despues de comprar panes, leche y huevos.
    
    Parametros:
    P -- numero de panes
    M -- numero de bolsas de leche
    H -- numero de huevos
    B -- valor del billete con el que se paga
    
    Retorna:
    un mensaje indicando el cambio o lo que queda debiendo.
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
P = int(input('Ingrese el numero de panes a comprar: '))
M = int(input('Ingrese el numero de bolsas de leche a comprar: '))
H = int(input('Ingrese el numero de huevos a comprar: '))
B = int(input('Ingrese el valor del billete con el que va a pagar: '))

# Llamar a la funcion y mostrar el resultado
print(calcular_cambio(P, M, H, B))

```

Este codigo solicitara al usuario los valores de P, M, H, y B y luego calculara el cambio o lo que queda debiendo despues de realizar la compra. Finalmente, mostrara un mensaje con el resultado.

______________________
## **Punto 5**:

Haga un programa que utilice una funcion para calcular el valor de un prestamo C usando interes compuesto del i por n meses.

```python
def calcular_valor_prestamo(C, i, n):
    """
    Calcula el valor acumulado de un prestamo utilizando interes compuesto.
    
    Parametros:
    C -- monto del prestamo inicial (capital)
    i -- tasa de interes mensual (en forma decimal, por ejemplo, 5% seria 0.05)
    n -- numero de meses
    
    Retorna:
    El valor futuro del prestamo.
    """
    A = C * (1 + i)**n
    return A

# Solicitar al usuario que ingrese los detalles del prestamo
C = float(input('Ingrese el monto del prestamo (capital inicial): '))
i = float(input('Ingrese la tasa de interes mensual (por ejemplo, ingrese 0.05 para 5%): '))
n = int(input('Ingrese el numero de meses: '))

# Calcular y mostrar el valor futuro del prestamo
valor_futuro = calcular_valor_prestamo(C, i, n)
print(f'El valor futuro del prestamo despues de {n} meses es: {valor_futuro}')

```

Este programa solicita que ingrese el capital inicial del prestamo, la tasa de interes mensual en forma decimal, y el numero de meses. Luego, usara la funcion *calcular_valor_prestamo* para calcular y mostrar el valor futuro del prestamo.

______________________
## **Punto 6**:

Para modelar el numero de personas contagiadas de Covid-19 en el pais de NuncaLandia, el cual dice que se duplica cada dia, vamos a usar una funcion exponencial. Entonces, La formula para calcular el numero total de contagiados despues de D dias seria:

C_total = C * 2^D



Aqui, C es el numero actual de contagiados y D es el numero de dias despues de hoy.

```python
def calcular_contagiados(C, D):
    """
    Calcula el numero total de personas contagiadas de Covid-19 despues de D dias.
    
    Parametros:
    C -- numero actual de contagiados
    D -- numero de dias despues de hoy
    
    Retorna:
    El numero total de personas contagiadas despues de D dias.
    """
    C_total = C * (2 ** D)
    return C_total

# Solicitar al usuario que ingrese el numero actual de contagiados y el numero de dias
C = int(input('Ingrese el numero actual de contagiados de Covid-19: '))
D = int(input('Ingrese el numero de dias a partir de hoy: '))

# Calcular y mostrar el numero total de contagiados despues de D dias
total_contagiados = calcular_contagiados(C, D)
print(f'El numero total de personas que se han contagiado despues de {D} dias es: {total_contagiados}')

```
Al ejecutar este programa, se pedira al usuario que ingrese el numero actual de contagiados y el numero de dias a futuro que desea calcular. Despues, el programa mostrara el total de personas contagiadas utilizando la funcion *calcular_contagiados*.

______________________
## **Punto 7**:

Escriba un programa que pida 5 numeros reales y calcule las siguientes operaciones usando una funcion para cada una:

+ El promedio
+ La mediana
+ El promedio multiplicativo (multilplica todos y luego calcula la raiz de la cantidad de operandos)
+ Ordenar los numeros de forma ascendente
+ Ordenar los numeros de forma descendente
+ La potencia del mayor numero elevado al menor numero
+ La raiz cubica del menor numero
  
```python
import math

def calcular_promedio(numeros):
    # Calcula el promedio de una lista de numeros
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    # Calcula la mediana de una lista de numeros
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

def calcular_promedio_multiplicativo(numeros):
    # Calcula el promedio multiplicativo de una lista de numeros
    producto = math.prod(numeros)
    return producto ** (1.0 / len(numeros))

def ordenar_ascendente(numeros):
    # Ordena la lista de numeros de forma ascendente
    return sorted(numeros)

def ordenar_descendente(numeros):
    # Ordena la lista de numeros de forma descendente
    return sorted(numeros, reverse=True)

def potencia_mayor_a_menor(numeros):
    # Calcula la potencia del mayor numero elevado al menor numero
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor_numero(numeros):
    # Calcula la raiz cubica del menor numero
    menor = min(numeros)
    return menor ** (1.0 / 3.0)

# Pedir al usuario que ingrese 5 numeros reales
numeros = []
for _ in range(5):
    numero = float(input("Ingrese un numero real: "))
    numeros.append(numero)

# Realizar los calculos y mostrar los resultados
print(f"Promedio: {calcular_promedio(numeros)}")
print(f"Mediana: {calcular_mediana(numeros)}")
print(f"Promedio multiplicativo: {calcular_promedio_multiplicativo(numeros)}")
print(f"Numeros ordenados de forma ascendente: {ordenar_ascendente(numeros)}")
print(f"Numeros ordenados de forma descendente: {ordenar_descendente(numeros)}")
print(f"Potencia del mayor numero elevado al menor numero: {potencia_mayor_a_menor(numeros)}")
print(f"Raiz cubica del menor numero: {raiz_cubica_menor_numero(numeros)}")

```
El programa pide al usuario que ingrese 5 numeros reales y despues llama a cada funcion para realizar los calculos requeridos y mostrar los resultados.

______________________
## **Punto 8**:
Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

(Se encuentran en los archivos del repo)
______________________
## **Punto 9**:
Consultar que es y como funciona pip en python.

`pip` es el sistema de gestion de paquetes utilizado por Python, que facilita la instalacion y gestion de bibliotecas y dependencias que no estan incluidas en la biblioteca estandar de Python. Su nombre es un acronimo recursivo que significa "Pip Installs Packages" (Pip Instala Paquetes).

### ¿Como funciona pip?
Cuando utilizas pip para instalar un paquete, realiza los siguientes pasos:

1. Busqueda del paquete: pip busca el paquete especificado en el Python Package Index (PyPI), que es un repositorio que contiene miles de paquetes de software para Python.

2. Resolucion de dependencias: Una vez encontrado el paquete, pip calcula y analiza las dependencias que el paquete necesita para funcionar correctamente. Esto significa que si el paquete que deseas instalar depende de otras librerias, pip intentara instalar esas librerias tambien.

3. Descarga del paquete y dependencias: pip descarga el paquete y cualquier dependencia necesaria desde PyPI.

4. Instalacion: Despues de la descarga, pip instala el paquete y sus dependencias en tu entorno Python. Esto incluye la compilacion de extensiones si es necesario.

5. Verificacion: Finalmente, pip verifica que la instalacion se haya completado correctamente.

### Uso basico de pip

Algunos comandos basicos de pip:

+ Instalar un paquete:
```Pseudocode
pip install nombre_del_paquete
```

+ Instalar una version especifica de un paquete:
```Pseudocode
pip install nombre_del_paquete==version
```

+ Actualizar un paquete:
```css
pip install --upgrade nombre_del_paquete
```

+ Desinstalar un paquete:
```pseudocode
pip uninstall nombre_del_paquete
```

+ Listar los paquetes instalados:
```pseudocode
pip list
```

+ Buscar paquetes en PyPI:
```sql
pip search termino_de_busqueda
```

Para utilizar `pip`, usualmente se necesita tener Python instalado en el sistema. `pip` se incluye por defecto con las versiones de Python 2.7.9+ y Python 3.4+. Para verificar si tenemos `pip` instalado y ver su version, podemos ejecutar pip --version en la linea de comandos o terminal.

______________________
## **Punto 10**:

1. Requests
+ **Uso**: Simplifica los metodos HTTP como GET y POST para realizar solicitudes a la web.
+ **Instalacion**:
```sh
pip install requests
```
2. NumPy
+ **Uso**: Proporciona soporte para arrays y matrices grandes y de alta dimension, junto con una coleccion de funciones matematicas para operar con estas estructuras.
+ **Instalacion**:
```sh
pip install numpy
```
3. Pandas
+ **Uso**: Ofrece estructuras de datos y herramientas de analisis de datos de alto rendimiento y facil uso.
+ **Instalacion**:
```sh
pip install pandas
```
4. Matplotlib
+ **Uso**: Libreria de trazado para Python y su extension matematica NumPy. Permite crear graficos estaticos, interactivos y animados.
+ **Instalacion**:
```sh
pip install matplotlib
```
5. SciPy
+ **Uso**: Basado en NumPy, agrega un monton de funcionalidades cientificas y tecnicas como modulos de optimizacion, algebra lineal, integracion, interpolacion, funciones especiales, FFT, procesamiento de señales y de imagenes, entre otros.
+ **Instalacion**:
```sh
pip install scipy
```
6. Flask
+ **Uso**: Microframework para aplicaciones web en Python. Es ligero y modular, lo que lo hace adaptable a las necesidades de desarrollo web.
+ **Instalacion**:
```sh
pip install Flask
```
7. Django
+ **Uso**:Framework de alto nivel para el desarrollo rapido de sitios web seguros y mantenibles. Fomenta el reuso de codigo y la modularidad.
+ **Instalacion**:
```sh
pip install Django
```
______________________
FIN DEL RETO
______________________
