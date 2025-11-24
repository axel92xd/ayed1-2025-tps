def binario_a_decimal(n):
    """
    Convierte un número binario (entero compuesto de 0s y 1s) a decimal.
    Pre: n es un número entero que representa un número binario (solo dígitos 0 y 1).
    Post: Devuelve el valor decimal correspondiente.
    """
    # Caso Base: Si el número es 0, su valor decimal es 0
    if n == 0:
        return 0
    
    # Tomamos el último dígito (n % 10)
    # Y le sumamos el resto del número convertido, multiplicado por 2
    # porque cada posición a la izquierda vale el doble en binario
    ultimo_digito = n % 10
    resto_del_numero = n // 10
    
    return ultimo_digito + 2 * binario_a_decimal(resto_del_numero)

def main():
    """
    Función principal para ejecutar el programa.
    Pregunta al usuario por un número binario y muestra su conversión a decimal.
    Pre: El usuario debe ingresar un número binario (solo dígitos 0 y 1).
    Post: Muestra el número decimal correspondiente.
    """
    numero_binario = int(input("Ingrese un número binario (solo 0s y 1s): "))
    numero_decimal = binario_a_decimal(numero_binario)
    print(f"El número decimal es: {numero_decimal}")
    
if __name__ == "__main__":
    main()