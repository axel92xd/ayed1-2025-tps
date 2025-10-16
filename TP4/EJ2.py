
def centrar_cadena(cadena: str, ancho: int = 80):
    """
    Imprime una cadena centrada en una línea del ancho especificado.
    Pre: cadena (str): La cadena de caracteres a centrar.
    Post: Ninguno. La función imprime directamente en la consola la cadena centrada y una línea de guiones del ancho especificado.
    """
    print("\n--- Cadena Centrada ---")
    print(cadena.center(ancho))
    print("-" * ancho)

def main():
    """
    Función principal para leer una cadena del usuario y mostrarla centrada.
    Pre: Ninguna, el programa solicitará la entrada al usuario.
    Post: Llama a la función centrar_cadena para imprimir el resultado en la consola.
    """
    texto_usuario = input("Ingrese la cadena de caracteres a centrar: ")
    centrar_cadena(texto_usuario)

if __name__ == "__main__":
    main()