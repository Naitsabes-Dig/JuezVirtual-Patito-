# Leer el número de elementos
n = int(input())

# Leer N números y guardarlos en una lista
numeros = []
for _ in range(n):
    numeros.append(int(input()))

# Imprimir cada número en una nueva línea
for numero in numeros:
    print(numero)