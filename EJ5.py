# Función lambda para número oblongo
oblongo = lambda x: any(n * (n + 1) == x for n in range(1, x))

# Función lambda para número triangular
triangular = lambda x: any(n * (n + 1) // 2 == x for n in range(1, x))

def main():
    # Pedir número al usuario
    numero = int(input("Ingrese un número entero positivo: "))

    # Validar precondiciones
    assert numero > 0, f"{numero} debe ser un entero positivo"

    # Probar oblongo
    if oblongo(numero):
        print(f"{numero} es un número oblongo.")
    else:
        print(f"{numero} no es un número oblongo.")

    # Probar triangular
    if triangular(numero):
        print(f"{numero} es un número triangular.")
    else:
        print(f"{numero} no es un número triangular.")


if __name__ == "__main__":
    main()
