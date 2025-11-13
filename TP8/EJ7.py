def gestionar_conjunto():
    """
    Crea un conjunto de números (0-9).
    Pide al usuario números para eliminar (usando .remove())
    y maneja el error (KeyError) si el número no existe.
    Termina con -1.
    
    Pre:  El usuario ingresa números enteros.
    Post: Muestra el estado del conjunto después de cada intento
          de eliminación.
    """
    
 
    numeros = set(range(10)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    print(f"Conjunto inicial: {numeros}")
    
    while True:
        try:
            valor_str = input("\nIngrese un número para eliminar (-1 para salir): ")
            valor = int(valor_str)
            
            if valor == -1:
                break
                
            # Intentamos eliminar con .remove()
            # Esto lanzará un 'KeyError' si el 'valor' no está.
            numeros.remove(valor)
            
            print(f"Elemento {valor} eliminado.")
            
        except ValueError:
            print("Error: Ingrese solo números enteros.")
        except KeyError:
            # Capturar el error si .remove() falla
            print(f"Error: El elemento {valor} NO existe en el conjunto.")
        
        print(f"Conjunto actual: {numeros}")

    print("\n--- Proceso finalizado ---")
    print(f"Conjunto final: {numeros}")

if __name__ == "__main__":
    gestionar_conjunto()