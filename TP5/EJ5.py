def calcular_raiz_cuadrada_segura():
    """
    Calcula la raíz cuadrada de un número ingresado por teclado.
    Usa el operador (**) en lugar del módulo 'math'.
    Maneja excepciones si se ingresa texto o un número negativo.
    
    Pre:  El usuario debe ingresar un valor por teclado.
    Post: Imprime la raíz cuadrada si el número es válido (>= 0).
          Imprime un mensaje de error específico si el número
          es negativo o si no es un número.
    """
    try:
        num_str = input("Ingrese un número (positivo): ")
        
        num_float = float(num_str)
        
        # Validamos que no sea negativo antes de calcular
        if num_float < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
            
        # Calculamos la raíz usando el operador de potencia
        # Elevar a 0.5 es lo mismo que la raíz cuadrada.
        resultado = num_float ** 0.5
        
        print(f"La raíz cuadrada de {num_float} es: {resultado}")
        
    except ValueError as e:
        # Captura el error de float("abc") O el que lanzamos nosotros
        print(f"Error: {e}.")

def main():
    """
    Programa principal para probar la función calcular_raiz_cuadrada_segura.
    Pre: No recibe parámetros.
    Post: Ejecuta pruebas de la función con entradas válidas e inválidas.
    """
    calcular_raiz_cuadrada_segura()


if __name__ == "__main__":
    main()