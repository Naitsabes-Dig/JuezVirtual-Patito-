def mover_puntos(archivos):
    n = len(archivos)  # Número de archivos en la lista

    # Función que verifica si los últimos dos son '.' y '..' (en cualquier orden)
    def esta_resuelto(v):
        return set(v[-2:]) == {'.', '..'}

    # Si ya están en las últimas posiciones, no hacemos nada
    if esta_resuelto(archivos):
        return archivos

    # Paso 2: intercambiar el primero que sea '.' o '..' con el último elemento
    for i in range(n):
        if archivos[i] == '.' or archivos[i] == '..':
            archivos[i], archivos[-1] = archivos[-1], archivos[i]  # Intercambia con el último
            break

    # Paso 3: si ahora están al final, se terminó
    if esta_resuelto(archivos):
        return archivos

    # Paso 4: buscar el primero que sea '.' o '..' y cambiarlo con el penúltimo
    for i in range(n):
        if archivos[i] == '.' or archivos[i] == '..':
            archivos[i], archivos[-2] = archivos[-2], archivos[i]  # Intercambia con el penúltimo
            break

    return archivos  # Devuelve la lista modificada

def main():
    T = int(input())  # Número de casos de prueba
    for caso in range(1, T+1):
        N = int(input())  # Número de archivos en este caso
        archivos = [input().strip() for _ in range(N)]  # Lee los nombres de los archivos
        resultado = mover_puntos(archivos)  # Aplica la función de ordenamiento
        print(f"Caso {caso}:")
        for archivo in resultado:
            print(archivo)  # Imprime cada archivo en el orden final
        print()  # espacio entre casos

# Ejecutar
main()
