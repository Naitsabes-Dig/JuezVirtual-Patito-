import sys

def count_peaks():
    try:
        # Lee el número de casos de prueba
        Q = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(Q):
        try:
            # Lee el número de puntos
            N = int(sys.stdin.readline())
            # Lee las alturas y las convierte a enteros
            heights = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            break

        peak_count = 0
        
        # Recorre la lista desde el segundo elemento hasta el penúltimo
        # El primer y último punto (valor 0) nunca pueden ser picos.
        for i in range(1, N - 1):
            if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
                peak_count += 1
        
        print(peak_count)

if __name__ == "__main__":
    count_peaks()