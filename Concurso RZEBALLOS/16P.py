def numero_armonico():
    # Lee el número entero n
    try:
        n = int(input())
    except (ValueError, EOFError):
        # Maneja casos en los que la entrada no es un número o está vacía
        return

    # Calcula el n-ésimo número armónico
    Hn = 0.0
    for i in range(1, n + 1):
        Hn += 1 / i

    # Imprime el resultado con 4 decimales de precisión
    print('{:.4f}'.format(Hn))

# Llama a la función principal
numero_armonico()