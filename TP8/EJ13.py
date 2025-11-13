def buscar_claves_por_valor(mi_diccionario: dict, valor_buscado) -> list:
    """
    Busca en un diccionario todas las claves que coincidan con un valor.
    
    Pre:  Recibe un diccionario y un valor a buscar.
    Post: Devuelve una LISTA de claves que "mapean" a ese valor.
          (La lista estará vacía si no se encuentra).
    """
    
    claves_encontradas = []
    
    # Iteramos sobre todos los pares (clave, valor) del diccionario
    for clave, valor_en_diccionario in mi_diccionario.items():
        
        # Si el valor del ítem es igual al que buscamos
        if valor_en_diccionario == valor_buscado:
            # agregamos la CLAVE a nuestra lista
            claves_encontradas.append(clave)
            
    return claves_encontradas


def main():
    """
    Función principal para ejecutar el ejercicio.
    Pre:  Ninguna.
    Post: Solicita un valor y muestra las claves que lo contienen.
    """
    # Diccionario de ejemplo (con valores repetidos)
    precios_frutas = {
        "Manzana": 150,
        "Banana": 200,
        "Naranja": 150,
        "Pera": 250,
        "Mandarina": 150
    }
    
    print(f"Diccionario: {precios_frutas}")
    
    try:
        valor_a_buscar = int(input("\nIngrese un precio (valor) para buscar: "))
        
        # Llamamos a la función
        lista_de_claves = buscar_claves_por_valor(precios_frutas, valor_a_buscar)
        
        if lista_de_claves: # Si la lista NO está vacía
            print(f"El valor {valor_a_buscar} fue encontrado en las claves:")
            print(lista_de_claves)
        else:
            print(f"No se encontró ninguna clave con el valor {valor_a_buscar}.")
            
    except ValueError:
        print("Error: Debe ingresar un número.")

if __name__ == "__main__":
    main()