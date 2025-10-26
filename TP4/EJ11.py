

def _contar_recursivo(cadena: str, subcadena: str) -> int:
    """
    Función auxiliar recursiva para contar las apariciones.
    Pre: cadena donde se realiza la búsqueda.
         Subcadena a buscar; puede ser la cadena vacía.
         Ambos parámetros deben ser strings; si se desea búsqueda case-insensitive,
          la cadena debe estar normalizada (por ejemplo, via .lower()) antes de llamar.

    Post: Número de ocurrencias de subcadena en cadena contando apariciones no consecutivas 
        - Si subcadena == "" devuelve 1.
    """
    
    #Si la subcadena está vacía, significa que encontramos una coincidencia completa.
    if not subcadena:
        return 1
    
    #Si la cadena principal se vació, pero aún buscamos algo, no hay coincidencia.
    if not cadena:
        return 0


    char_a_buscar = subcadena[0]
    resto_subcadena = subcadena[1:]
    
    total_coincidencias = 0
    
    # Buscamos el primer caracter en lo que queda de la cadena
    for i in range(len(cadena)):
        if cadena[i] == char_a_buscar:
            # Si lo encontramos, buscamos el resto de la subcadena
            # en el resto de la cadena principal.
            total_coincidencias += _contar_recursivo(cadena[i + 1:], resto_subcadena)
            
    return total_coincidencias

def contar_subcadena_no_consecutiva(cadena_original: str, subcadena_original: str) -> int:
    """
    Cuenta cuántas veces aparece una subcadena no consecutiva dentro de una cadena.

    Pre: El texto donde se buscará y la subcadena que se quiere encontrar.

    Post: El número de veces que la subcadena fue encontrada, sin distinguir mayúsculas/minúsculas y sin ser consecutiva.
    """

    cadena = cadena_original.lower()
    subcadena = subcadena_original.lower()
    
    return _contar_recursivo(cadena, subcadena)


def main():
    """
    Función principal para verificar el comportamiento de la función
    de contar subcadenas.
    """
    
    cadena_larga = input("Ingrese una cadena larga: ")
    subcadena_uade = input("Ingrese la subcadena a buscar: ")
    
    cantidad = contar_subcadena_no_consecutiva(cadena_larga, subcadena_uade)
    
    print(f"\nCantidad encontrada: {cantidad}") 
    


if __name__ == "__main__":
    main()