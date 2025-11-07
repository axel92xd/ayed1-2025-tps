def buscar_en_lista_con_errores():
    """
    Carga una lista de enteros (terminando con -1).
    Luego permite buscar números usando list.index().
    Aborta la búsqueda al tercer error (número no encontrado o inválido).
    
    Pre:  El usuario ingresa números para la lista, y luego números para buscar.
    Post: Muestra la posición (índice) de los números encontrados.
          Se detiene si el usuario comete 3 errores de búsqueda consecutivos.
    """
    
    numeros = []
    print("Ingrese números enteros (termine con -1):")
    while True:
        try:
            num_str = input("> ")
            num = int(num_str)
            
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Error: Ingrese solo números enteros.")
            
    if not numeros:
        print("La lista está vacía. Fin del ejercicio.")
        return
        
    print(f"\nLista cargada: {numeros}")


    print("\n--- Iniciando Búsqueda (3 intentos fallidos máx) ---")
    error_count = 0
    while error_count < 3:
        try:
            num_buscar_str = input("Ingrese un número para buscar (o -1 para salir): ")
            num_buscar = int(num_buscar_str)
            
            if num_buscar == -1:
                break
            
            # Usamos list.index() directamente, sin usar el operador 'in'.
            # Esto lanzará un ValueError si no lo encuentra.
            posicion = numeros.index(num_buscar)
            
            print(f"¡Éxito! El número {num_buscar} se encuentra en la posición {posicion}.")
    
            error_count = 0 
            
        except ValueError:
            # Captura el error de int() O el de numeros.index()
            error_count += 1
            print(f"Error: El número no es válido o no se encuentra en la lista.")
            print(f"Intentos fallidos: {error_count}/3")
            
    if error_count == 3:
        print("\nDemasiados errores de búsqueda. Abortando.")

def main():
    """
    Programa principal para probar la función buscar_en_lista_con_errores.
    Pre: No recibe parámetros.
    Post: Ejecuta la función de búsqueda con manejo de errores.
    """
    buscar_en_lista_con_errores()

if __name__ == "__main__":
    main()