import sys

def suma_digitos(num):
    """Calculates the sum of the digits of a number."""
    return sum(int(digit) for digit in str(num))

def generar_serie(n):
    """
    Generates the first n numbers of the series.
    """
    if n <= 0:
        return []

    serie = [35]
    if n == 1:
        return serie

    num_actual = 35
    
    for i in range(1, n):
        if i % 2 != 0:
            # Odd positions (2nd, 4th, etc.) get the sum of digits of the previous number.
            num_actual = suma_digitos(num_actual)
        else:
            # Even positions (3rd, 5th, etc.) get the sum of the previous two numbers.
            # This requires a bit of state management.
            if len(serie) >= 2:
                num_actual = serie[-1] + serie[-2]
            else:
                # Fallback for the third number if the pattern is slightly different
                # in the first few terms.
                num_actual = serie[-1] + suma_digitos(serie[-1])

        serie.append(num_actual)
    
    return serie

def main():
    """
    Main function to handle test cases.
    """
    try:
        num_casos_prueba = int(sys.stdin.readline())
        
        for _ in range(num_casos_prueba):
            n = int(sys.stdin.readline())
            
            if n > 0:
                resultado = generar_serie(n)
                # Print the series with two spaces between numbers
                print("  ".join(map(str, resultado)))
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()