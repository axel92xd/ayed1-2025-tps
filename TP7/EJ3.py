def suma_naturales(n):
    """
    Devuelve la suma de los primeros N números (1 + 2 + ... + n).
    Pre:: n es un número natural (n >= 0).
    Post:: Retorna la suma de los primeros N números naturales.
    """
    if n == 0:
        return 0
    
    
    return n + suma_naturales(n - 1)

def main():
    """
    Función principal para ejecutar el programa.
    Pregunta al usuario por un número natural y muestra la suma de los primeros N números naturales.
    Pre:: El usuario debe ingresar un número natural (n >= 0).
    Post:: Muestra la suma de los primeros N números naturales.
    """
    
    numero = int(input("Ingrese un número natural: "))
    resultado = suma_naturales(numero)
    print(f"La suma de los primeros {numero} números naturales es: {resultado}")

if __name__ == "__main__":
    main()