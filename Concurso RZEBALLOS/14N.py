# Leer un solo caracter del teclado
character = input()

# Comprobar si la letra es minúscula
if 'a' <= character <= 'z':
    # Convertir a mayúscula
    print(character.upper())
# Comprobar si la letra es mayúscula
elif 'A' <= character <= 'Z':
    # Convertir a minúscula
    print(character.lower())