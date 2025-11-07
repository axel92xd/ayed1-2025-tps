def ingresar_numero_natural() -> int:
    """
    Solicita al usuario un número natural (entero > 0) por teclado.
    Rechaza ingresos inválidos usando excepciones y muestra la razón del error.
    
    Pre:  El usuario debe ingresar datos por teclado.
    Post: Devuelve el número (int) validado, garantizando que sea entero y > 0.
          Si el dato es inválido, muestra la razón exacta del error y
          vuelve a solicitarlo.
    """
    while True:
        try:
            entrada_str = input("Ingrese un número natural (entero y mayor que 0): ")
            
            num_int = int(entrada_str)
            
            # Controlamos que sea mayor que 0
            if num_int <= 0:
                # Lanzamos nuestra propia excepción para ser capturada abajo
                raise ValueError("El número debe ser mayor que 0.")
                
            return num_int
            
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")

def main():
    """
    Programa principal para probar la función ingresar_numero_natural.
    Pre: No recibe parámetros.
    Post: Muestra el número natural ingresado correctamente.
    """

    numero_valido = ingresar_numero_natural()
    print(f"¡Número correcto ingresado: {numero_valido}!")

if __name__ == "__main__":
    main()