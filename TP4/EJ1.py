def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicúa sin usar rebanadas ni cadenas auxiliares.

    Un capicúa (o palíndromo) se lee igual de izquierda a derecha que de
    derecha a izquierda. Esta función utiliza dos índices que se mueven
    desde los extremos hacia el centro para comparar los caracteres.

    Pre: `cadena` es un string.
    Post: Devuelve True si es capicúa, False en caso contrario.
    """
    # Se inicializan dos índices: uno al principio y otro al final de la cadena.
    izquierda = 0
    derecha = len(cadena) - 1

    while izquierda < derecha:
    
        if cadena[izquierda] != cadena[derecha]:
            return False
        
        izquierda += 1
        derecha -= 1
    return True


def main():
    cadena_usuario = input("Ingrese la cadena: ")
    if es_capicua(cadena_usuario):
        print("Es capicúa.")
    else:
        print("No es capicúa.")

if __name__ == "__main__":
    main()