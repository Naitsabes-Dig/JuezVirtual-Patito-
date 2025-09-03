def obtCantPref(n):     
    # Crea una lista con el primer carácter de cada palabra en n
    pre = []
    for i in n:
        pre.append(i[0])
    letra = []
    mayor = 0
    # Recorre los caracteres y cuenta cuántas veces aparece cada uno
    for i in pre:       
        if i in letra:  # Si ya se contó esta letra, continúa
            continue
        letra.append(i) # Agrega la letra a la lista de letras contadas
        nu = pre.count(i) # Cuenta cuántas veces aparece la letra
        if nu > mayor:    # Si es la mayor cantidad hasta ahora, actualiza
            mayor = nu
    return mayor         # Devuelve la mayor cantidad encontrada


casos = int(input()) # Lee el número de casos
for i in range(casos):
    jug = []
    num = int(input()) # Lee el número de jugadores
    cant = []
    mayor = 0
    for j in range(num):            
        frase = input().split() # Lee la frase y la divide en palabras
        nu = obtCantPref(frase) # Obtiene la mayor cantidad de palabras con el mismo prefijo
        if nu > mayor:          # Actualiza el mayor si es necesario
            mayor = nu
        cant.append(nu)         # Guarda el resultado para cada jugador
    print("El ganador es "+str(cant.index(mayor)+1)) # Imprime el ganador (posición + 1)