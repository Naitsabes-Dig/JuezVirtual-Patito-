def es_bisiesto(year):
    """
    Determina si un año es bisiesto según las reglas del calendario Gregoriano.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def es_fecha_valida(day, month, year):
    """
    Valida si una fecha es correcta.
    """
    # Rango del año
    if not (1 <= year):
        return False

    # Rango del mes
    if not (1 <= month <= 12):
        return False

    # Días en cada mes
    dias_en_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ajusta los días para febrero en un año bisiesto
    if es_bisiesto(year):
        dias_en_mes[2] = 29
    
    # Rango del día
    if not (1 <= day <= dias_en_mes[month]):
        return False
    
    return True

def main():
    """
    Función principal para leer la entrada y procesar las fechas.
    """
    try:
        # Lee el número de fechas a verificar
        num_fechas = int(input())
        
        # Procesa cada fecha
        for _ in range(num_fechas):
            day, month, year = map(int, input().split())
            
            if es_fecha_valida(day, month, year):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
                
    except (ValueError, IndexError):
        # Maneja errores de formato de entrada
        pass

if __name__ == "__main__":
    main()