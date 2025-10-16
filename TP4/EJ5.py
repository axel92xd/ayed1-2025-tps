# --- Versión 5a: Utilizando sólo ciclos normales ---
def filtrar_palabras_ciclo(frase: str, n: int) -> str:
    """
    Filtra palabras de una frase que tengan N o más caracteres.

    Pre: frase (str): La cadena de caracteres a procesar.
         n (int): El número mínimo de caracteres que debe tener una palabra.
    Post: (str): Una nueva cadena con solo las palabras que cumplen la condición.
    """
    palabras = frase.split()
    palabras_filtradas = []
    for palabra in palabras:
        if len(palabra) >= n:
            palabras_filtradas.append(palabra)
    return " ".join(palabras_filtradas)

#Utilizando listas por comprensión ---
def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    Filtra palabras de una frase que tengan N o más caracteres.

    Pre: frase (str): La cadena de caracteres a procesar.
         n (int): El número mínimo de caracteres que debe tener una palabra.
    Post: (str): Una nueva cadena con solo las palabras que cumplen la condición.
    """
    palabras_filtradas = [palabra for palabra in frase.split() if len(palabra) >= n]
    return " ".join(palabras_filtradas)

#Utilizando la función filter ---
def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    Filtra palabras de una frase que tengan N o más caracteres.

    Pre: frase (str): La cadena de caracteres a procesar.
        n (int): El número mínimo de caracteres que debe tener una palabra.
    Post: (str): Una nueva cadena con solo las palabras que cumplen la condición.
    """
    palabras_filtradas = filter(lambda palabra: len(palabra) >= n, frase.split())
    return " ".join(palabras_filtradas)

def main():
    """
    Función principal para filtrar palabras de una frase dada.
    """
    frase_usuario = input("Ingrese una frase: ")
    try:
        longitud_minima = int(input("Ingrese la longitud mínima de caracteres: "))

        print("\nResultados:")
        # Prueba la versión con ciclo normal
        resultado_a = filtrar_palabras_ciclo(frase_usuario, longitud_minima)
        print(f"  a) Usando ciclos:     {resultado_a}")

        # Prueba la versión con listas por comprensión
        resultado_b = filtrar_palabras_comprension(frase_usuario, longitud_minima)
        print(f"  b) Usando comprensión:   {resultado_b}")

        # Prueba la versión con la función filter
        resultado_c = filtrar_palabras_filter(frase_usuario, longitud_minima)
        print(f"  c) Usando filter:        {resultado_c}")

    except ValueError:
        print("Error: La longitud debe ser un número entero.")

if __name__ == "__main__":
    main()