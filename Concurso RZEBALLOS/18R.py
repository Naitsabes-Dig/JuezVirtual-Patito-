import sys

def largest_prime_factor(n):
    """
    Calcula el factor primo más grande de un número entero n.
    """
    largest_prime = 1
    
    # 1. Manejar el factor 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
        
    # 2. Manejar factores primos impares
    # Los factores primos de un número (excepto el 2) son impares.
    # Solo necesitamos verificar hasta la raíz cuadrada del número.
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2
        
    # 3. Si n es un número primo mayor a 2
    # Si después de las divisiones n es mayor que 2,
    # el n restante es el factor primo más grande.
    if n > 2:
        largest_prime = n
        
    return largest_prime

def main():
    """
    Función principal para procesar múltiples casos de prueba.
    """
    for line in sys.stdin:
        try:
            n = int(line.strip())
            if n > 1:
                result = largest_prime_factor(n)
                print(result)
        except (ValueError, IndexError):
            # Termina si la línea no es un número válido
            break

if __name__ == "__main__":
    main()