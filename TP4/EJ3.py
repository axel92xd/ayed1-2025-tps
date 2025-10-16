# --- Definición de la Función Lógica ---
def separar_clave_maestra(clave_maestra_str: str) -> tuple[int, int]:
    """
    Separa los dígitos de una clave maestra en dos claves secundarias.

    Pre: Una cadena que debe contener únicamente caracteres numéricos ('0'-'9').
    Post: Devuelve una tupla con dos números enteros. El primero se forma con los dígitos de las posiciones impares y
    el segundo con los de las posiciones pares.
    """
    clave1_str = ""
    clave2_str = ""

    for i, digito in enumerate(clave_maestra_str):
        posicion = i + 1
        if posicion % 2 != 0:
            clave1_str += digito
        else:
            clave2_str += digito

    if clave1_str:  # Esto pregunta si la cadena no está vacía
        clave1_int = int(clave1_str)
    else:
        clave1_int = 0
    
    if clave2_str:  
        clave2_int = int(clave2_str)
    else:
        clave2_int = 0

    return (clave1_int, clave2_int)

def main():
    """
    Función principal para leer una clave maestra y mostrar las claves separadas.
    """
    clave_maestra_input = input("Ingrese el número de la clave maestra: ")

    if clave_maestra_input.isdigit():
        clave1, clave2 = separar_clave_maestra(clave_maestra_input)
        print(f"\nDe la clave maestra '{clave_maestra_input}':")
        print(f"-> La clave 1 (dígitos en posiciones impares) es: {clave1}")
        print(f"-> La clave 2 (dígitos en posiciones pares) es: {clave2}")
    else:
        print("Error: La entrada debe ser un número entero positivo.")


if __name__ == "__main__":
    main()