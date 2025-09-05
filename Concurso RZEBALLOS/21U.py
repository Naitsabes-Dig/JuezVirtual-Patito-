def es_array_palindrome():
    try:
        # Leer el tamaño del array
        n = int(input())
        
        # Leer los elementos del array
        arr = list(map(int, input().split()))

        # Invertir el array
        arr_invertido = arr[::-1]
        
        # Comparar el array original con el invertido
        if arr == arr_invertido:
            print("SI")
        else:
            print("NO")
            
    except (IOError, ValueError):
        # Maneja posibles errores en la entrada
        pass

# Ejecuta la función
es_array_palindrome()