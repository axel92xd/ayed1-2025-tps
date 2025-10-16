# --- Versión 6a: Utilizando rebanadas ---
def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena utilizando rebanadas (slicing).

    Pre: cadena (str): La cadena original.
         posicion (int): El índice de inicio (0-based).
         cantidad (int): El número de caracteres a extraer.
    Post: (str): La subcadena extraída.
    """
    return cadena[posicion : posicion + cantidad]

#Sin utilizar rebanadas 
def extraer_subcadena_ciclo(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena utilizando un ciclo, sin rebanadas.

    Pre: cadena (str): La cadena original.
         posicion (int): El índice de inicio (0-based).
         cantidad (int): El número de caracteres a extraer.
    Post: (str): La subcadena extraída.
    """
    subcadena_resultado = ""
    for i in range(cantidad):
        # Nos aseguramos de no intentar acceder a un índice fuera de la cadena
        if posicion + i < len(cadena):
            subcadena_resultado += cadena[posicion + i]
    return subcadena_resultado


def main():
    """
    Función principal para extraer una subcadena de una cadena dada.
    """
    cadena_ejemplo = "El número de teléfono es 4356-7890"
    print(f"Cadena de ejemplo: '{cadena_ejemplo}'")

    try:
        pos = int(input("Ingrese la posición inicial: "))
        cant = int(input("Ingrese la cantidad de caracteres: "))

        print("\nResultados:")
        resultado_a = extraer_subcadena_rebanadas(cadena_ejemplo, pos, cant)
        print(f"  a) Usando rebanadas: '{resultado_a}'")

        resultado_b = extraer_subcadena_ciclo(cadena_ejemplo, pos, cant)
        print(f"  b) Sin usar rebanadas: '{resultado_b}'")

    except ValueError:
        print("Error: La posición y la cantidad deben ser números enteros.")

if __name__ == "__main__":
    main()