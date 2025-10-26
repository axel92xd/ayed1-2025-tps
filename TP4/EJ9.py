import string 

def longitud_sin_puntuacion(palabra: str) -> int:
    """
    Calcula la longitud "efectiva" de una palabra, ignorando los signos de puntuación.
    Versión simple SIN expresiones regulares.

    Pre: Una palabra que puede contener signos de puntuación.
    Post: El conteo de caracteres de la palabra que NO son signos de puntuación.
    """
    longitud_efectiva = 0
    for caracter in palabra:
        if caracter not in string.punctuation:
            longitud_efectiva += 1
    return longitud_efectiva

def ordenar_palabras_por_longitud(frase: str) -> str:
    """
    Ordena las palabras de una frase por su longitud efectiva (sin puntuación).

    Pre: Una cadena con palabras separadas por uno o más espacios.
    Post: Una nueva cadena con las palabras ordenadas de menor a mayor longitud efectiva, separadas por un solo espacio.
    """

    palabras = frase.split()
    palabras_ordenadas = sorted(palabras, key=longitud_sin_puntuacion)
    
    return " ".join(palabras_ordenadas)

def main():
    """
    Función principal para verificar el comportamiento de la función
    de ordenar palabras.
    """
    frase_ejemplo = input("Ingrese una frase: ")
    print(f"Frase original: '{frase_ejemplo}'")
    
    frase_resultante = ordenar_palabras_por_longitud(frase_ejemplo)
    
    print(f"Frase ordenada: '{frase_resultante}'")


if __name__ == "__main__":
    main()