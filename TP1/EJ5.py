
def es_oblongo(x: int) -> bool:
    """
    Determina si un número es oblongo (producto de dos enteros consecutivos).

    Pre: x > 0
    Post: Devuelve True si x es oblongo, False en caso contrario.
    """
    assert isinstance(x, int) and x > 0, "El número debe ser un entero positivo"

    n = 1
    while n * (n + 1) <= x:
        if n * (n + 1) == x:
            return True
        n += 1
    return False


def es_triangular(x: int) -> bool:
    """
    Determina si un número es triangular (suma de los primeros n naturales).

    Pre: x > 0
    Post: Devuelve True si x es triangular, False en caso contrario.
    """
    assert isinstance(x, int) and x > 0, "El número debe ser un entero positivo"

    n = 1
    while n * (n + 1) // 2 <= x:
        if n * (n + 1) // 2 == x:
            return True
        n += 1
    return False


def main():
    numero = int(input("Ingrese un número entero positivo: "))
    assert numero > 0, f"{numero} debe ser un entero positivo"

    if es_oblongo(numero):
        print(f"{numero} es un número oblongo.")
    else:
        print(f"{numero} no es un número oblongo.")

    if es_triangular(numero):
        print(f"{numero} es un número triangular.")
    else:
        print(f"{numero} no es un número triangular.")


if __name__ == "__main__":
    main()
