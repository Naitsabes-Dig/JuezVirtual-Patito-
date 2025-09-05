import sys

def solve():
    """
    Lee los casos de prueba y calcula la serie de números hexagonales centrados.
    """
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            n = int(sys.stdin.readline())
            
            resultados = []
            for i in range(1, n + 1):
                # Usa la fórmula para el n-ésimo número hexagonal centrado
                monedas = i * (2 * i - 1)
                resultados.append(str(monedas))
            
            print(" ".join(resultados))
    
    except (IOError, ValueError):
        pass

solve()