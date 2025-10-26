# --- Definición de la Función Lógica ---
def reemplazar_palabra_completa(cadena_original: str, palabra_a_buscar: str, palabra_reemplazo: str) -> tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa por otra.
    Versión simple SIN expresiones regulares.

    Pre: El texto donde se buscará.
         La palabra completa que se quiere reemplazar.
         La nueva palabra que se usará.
    Post: Una tupla que contiene:
            1. La cadena de caracteres con los reemplazos hechos.
            2. Un entero con la cantidad de reemplazos realizados.
    """

    palabras = cadena_original.split()
    
    palabras_nuevas = [] 
    cantidad = 0

    for palabra in palabras:
        # Comparamos si la palabra es exactamente la que buscamos
        if palabra == palabra_a_buscar:
            # Si es, agregamos la palabra de reemplazo y contamos
            palabras_nuevas.append(palabra_reemplazo)
            cantidad += 1
        else:
            # Si no es, simplemente agregamos la palabra original
            palabras_nuevas.append(palabra)
            
    # 4. Unimos la nueva lista para formar la cadena final
    nueva_cadena = " ".join(palabras_nuevas)
    
    return nueva_cadena, cantidad

def main():
    """
    Función principal para verificar el comportamiento de la función
    de reemplazar palabras.
    """

    texto = input("Ingrese un texto de prueba: ")
    buscar = input("Ingrese la palabra a buscar: ")
    reemplazar = input("Ingrese la palabra de reemplazo: ")
    
    print(f"Texto original:\n'{texto}'")
    print(f"Palabra a buscar: '{buscar}'")
    print(f"Palabra a reemplazar: '{reemplazar}'")
    
    texto_resultante, num_reemplazos = reemplazar_palabra_completa(texto, buscar, reemplazar)
    
    print(f"\nTexto resultante:\n'{texto_resultante}'")
    print(f"Total de reemplazos: {num_reemplazos}")


if __name__ == "__main__":
    main()