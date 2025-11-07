def obtener_nombre_mes(numero_mes: int) -> str:
    """
    Devuelve una cadena con el nombre del mes.
    
    Pre:  Recibe un número de mes (int).
    Post: Devuelve el nombre del mes (str) en minúsculas.
          Devuelve una cadena vacía (str) si el número de mes es inválido
          (fuera del rango 1-12), detectado mediante una excepción.
    """
    
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    
    try:
        if numero_mes < 1:
            
            raise IndexError("El número de mes debe ser 1 o mayor.")
            
        # Accedemos al mes. (mes 1 = índice 0)
        # Si numero_mes es 13 o más, lanzará un IndexError automáticamente
        return meses[numero_mes - 1]
        
    except IndexError:
        return "" # Cadena vacía si el mes es inválido

def main():
    """
    Programa principal para probar la función obtener_nombre_mes.
    Pre: No recibe parámetros.
    Post: Muestra resultados de pruebas con meses válidos e inválidos.
    """

    mes = int(input("Ingrese un número de mes (1-12): "))
    nombre_mes = obtener_nombre_mes(mes)
    if nombre_mes:
        print(f"El mes {mes} es '{nombre_mes}'.")
    else:
        print(f"Error: El número de mes {mes} es inválido.")
if __name__ == "__main__":
    main()