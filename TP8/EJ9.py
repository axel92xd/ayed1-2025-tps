def mostrar_tabla_multiplicar():
    """
    Pide un número N y genera su tabla de multiplicar (1-12)
    usando un diccionario por comprensión.
    
    Pre:  El usuario ingresa un número entero.
    Post: Imprime la tabla de multiplicar con formato.
    """
    
    try:
        n = int(input("Ingrese un número entero (N) para ver su tabla: "))
        
        # Diccionario por Comprensión 
        tabla = {i: n * i for i in range(1, 13)}

        # Mostrar la tabla con formato
        print(f"\n--- Tabla del {n} ---")
        for multiplicador, resultado in tabla.items():
            # Usamos f-strings para alinear el texto
            print(f"{n:>2} x {multiplicador:>2} = {resultado:>3}")
            
    except ValueError:
        print("Error: Debe ingresar un número entero.")


def main():
    """
    Función principal para ejecutar el ejercicio.
    Pre:  Ninguna.
    Post: Ejecuta la función para mostrar la tabla de multiplicar.
    """
    mostrar_tabla_multiplicar()

if __name__ == "__main__":
    main()