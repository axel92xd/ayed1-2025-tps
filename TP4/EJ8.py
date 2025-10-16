def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos N caracteres de una cadena.

    Pre: cadena (str): La cadena original.
         n (int): El número de caracteres a devolver desde el final.
    Post: (str): La subcadena con los últimos N caracteres. Si N es mayor que la longitud de la cadena, devuelve la cadena completa.
    """
    # Usar un índice negativo en una rebanada cuenta desde el final.
    return cadena[-n:]


def main():
    """
    Función principal para obtener los últimos N caracteres de una cadena.
    """
    cadena_usuario = input("Ingrese una cadena de caracteres: ")
    try:
        n_caracteres = int(input("Ingrese la cantidad de caracteres a obtener del final: "))
        
        if n_caracteres < 0:
            print("Error: El número de caracteres no puede ser negativo.")
        else:
            resultado = ultimos_n_caracteres(cadena_usuario, n_caracteres)
            print(f"\nLos últimos {n_caracteres} caracteres son: '{resultado}'")

    except ValueError:
        print("Error: La cantidad de caracteres debe ser un número entero.")

if __name__ == "__main__":
    main()