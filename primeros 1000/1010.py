n = int(input())  # Lee el número de casos de prueba
pal = "UMSAICPC"  # Palabra objetivo a buscar
aux = ''          # Variable auxiliar para construir la palabra encontrada

for i in range(n):
    x = input()   # Lee la cadena de entrada para cada caso
    for item in pal:
        # Busca la letra 'item' en la cadena 'x'
        if(x.find(item) != -1):
            index = x.find(item)  # Obtiene el índice de la letra encontrada
            # Elimina la letra encontrada de la cadena 'x'
            x = x[0:index] + x[index+1:]
            # Añade la letra encontrada a 'aux'
            aux = aux + item
    # Verifica si se pudo formar la palabra objetivo
    if aux == pal:
        print('ES POSIBLE')
    else:
        print('NO ES POSIBLE')
    aux = ''  # Reinicia la variable auxiliar para el siguiente caso