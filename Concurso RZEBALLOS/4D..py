# Leer la cantidad de carros
n = int(input())

# Iterar sobre cada carro
for _ in range(n):
    # Leer el tiempo y la velocidad
    d, v = map(float, input().split())
    
    # Calcular la longitud del carro
    longitud = d * v
    
    # Imprimir la longitud con 3 decimales
    print(f"{longitud:.3f}")