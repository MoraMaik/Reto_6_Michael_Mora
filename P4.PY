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

# Solicitar que ingrese las cantidades y el billete con el que va a pagar
P = int(input('Ingrese el número de panes a comprar: '))
M = int(input('Ingrese el número de bolsas de leche a comprar: '))
H = int(input('Ingrese el número de huevos a comprar: '))
B = int(input('Ingrese el valor del billete con el que va a pagar: '))

# Llamar a la función y mostrar el resultado
print(calcular_cambio(P, M, H, B))
