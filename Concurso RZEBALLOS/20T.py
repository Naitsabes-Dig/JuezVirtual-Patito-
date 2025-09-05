import sys

def es_capicua():
    """
    Verifica si un número es capicúa.
    """
    try:
        # Lee el número como una cadena de texto para manejar números grandes
        num_str = sys.stdin.readline().strip()
        
        # Compara la cadena original con su versión invertida
        if num_str == num_str[::-1]:
            print('S')
        else:
            print('N')
    except (IOError, ValueError):
        # Maneja posibles errores en la entrada
        pass

if __name__ == "__main__":
    es_capicua()