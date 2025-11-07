def sumar_cadenas_reales(str1: str, str2: str) -> float | int:
    """
    Suma dos números reales (float) contenidos en cadenas de caracteres.
    
    Pre:  Recibe dos cadenas de caracteres (str1, str2).
    Post: Devuelve la suma (float) de ambas cadenas convertidas.
          Devuelve -1 (int) si alguna de las cadenas no contiene un 
          número real válido (ej: "abc" o "10,5" con coma).
    """
    try:
        num1 = float(str1)
        num2 = float(str2)
        return num1 + num2
    except ValueError:
        return -1

def main():
    """
    Programa principal para probar la función sumar_cadenas_reales.
    Pre: No recibe parámetros.
    Post: Muestra resultados de pruebas con casos válidos e inválidos.
    """
    
    # Caso válido
    res1 = sumar_cadenas_reales("10.5", "5")
    print(f"Prueba 1 ('10.5', '5'): Resultado = {res1}")
    
    # Caso inválido (texto)
    res2 = sumar_cadenas_reales("abc", "10")
    print(f"Prueba 2 ('abc', '10'): Resultado = {res2}")
    
    # Caso inválido (coma en lugar de punto)
    res3 = sumar_cadenas_reales("20,7", "10")
    print(f"Prueba 3 ('20,7', '10'): Resultado = {res3}")

if __name__ == "__main__":
    main()