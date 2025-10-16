# --- Definición de la Función Lógica ---
def a_romano(numero: int) -> str:
    """
    Convierte un número entero entre 0 y 3999 a su representación en números romanos.

    Pre: Un número entero.
    Post: Si `numero` está en [0, 3999], devuelve su representación romana. En otro caso, devuelve un mensaje de error.
    """
    if not 0 <= numero <= 3999:
        return "Error: El número debe estar entre 0 y 3999."
    if numero == 0:
        return "No existe representación estándar para el cero."

    mapa_romano = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
        (4, 'IV'), (1, 'I')
    ]
    resultado_romano = ""
    for valor, simbolo in mapa_romano:
        while numero >= valor:
            resultado_romano += simbolo
            numero -= valor
    return resultado_romano

def main():
    """
    Función principal para leer un número del usuario y convertirlo a romano.
    """
    try:
        num_usuario = int(input("Ingrese un número entero entre 0 y 3999: "))
        romano = a_romano(num_usuario)
        print(f"El número {num_usuario} en romano es: {romano}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


if __name__ == "__main__":
    main()