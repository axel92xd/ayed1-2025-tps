def contar_digitos(n):
    """
    Cuenta la cantidad de dígitos de un número entero de forma recursiva.
    Pre: n es un entero.
    Post: Devuelve la cantidad de dígitos.
    """
    n = abs(n) # Trabajamos con el valor absoluto para ignorar el signo menos
    
    # Caso Base: Si el número tiene un solo dígito (es menor a 10)
    if n < 10:
        return 1
    
    return 1 + contar_digitos(n // 10)

def main():
    """
    Pregunta al usuario por un número entero y muestra la cantidad de dígitos que tiene.
    Pre: El usuario debe ingresar un número entero.
    Post: Muestra la cantidad de dígitos del número ingresado.
    """
    numero = int(input("Ingrese un número entero: "))
    cantidad_digitos = contar_digitos(numero)
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

if __name__ == "__main__":
    main()