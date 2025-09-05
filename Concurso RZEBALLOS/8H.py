n = int(input())

# Calculamos el último múltiplo de 3 menor que n
ultimo = (n - 1) // 3 * 3

# Número de múltiplos de 3 menores que n
k = ultimo // 3

# Suma de los múltiplos de 3 usando fórmula de suma de progresión aritmética
suma3 = 3 * k * (k + 1) // 2

print(suma3)