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
