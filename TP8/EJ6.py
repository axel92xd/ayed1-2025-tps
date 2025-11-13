import string # Para importar los signos de puntuación

def procesar_frase():
    """
    Lee una frase, elimina repetidas usando un set y
    muestra las palabras ordenadas por su longitud.
    
    Pre:  El usuario ingresa una frase por teclado.
    Post: Imprime la lista de palabras únicas, ordenadas por longitud.
    """
    
    frase = input("Ingrese una frase: ")
    
    # Limpiar la frase de signos de puntuación
    # (Creamos una "tabla de traducción" que reemplaza
    # cada signo de puntuación por 'None' (nada))
    tabla_puntuacion = str.maketrans('', '', string.punctuation)
    frase_limpia = frase.translate(tabla_puntuacion)
    
    # Convertir a minúsculas y separar en palabras
    palabras_lista = frase_limpia.lower().split()
    
    palabras_unicas = set(palabras_lista)
    
    lista_para_ordenar = list(palabras_unicas)
    
    # Ordenar la lista usando 'key=len'
    # 'key=len' le dice a sorted() que ordene basándose
    # en el resultado de la función len() aplicada a cada palabra.
    lista_ordenada = sorted(lista_para_ordenar, key=len)
    
    print("\n--- Palabras únicas ordenadas por longitud ---")
    print(lista_ordenada)


def main():
    """
    Función principal para ejecutar el procesamiento de la frase.
    Pre:  ninguna.
    Post: llama a la función que procesa la frase.
    """
    procesar_frase()

if __name__ == "__main__":
    main()