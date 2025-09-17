def lista_cuadrados() -> List[int]:
    """
    Crea una lista con los cuadrados de los números del 1 a N.

    Pre: N > 0 ingresado por teclado
    Post: Devuelve lista de cuadrados de tamaño N
    """
    N = int(input("\nIngrese un número N: "))
    assert N > 0, "N debe ser mayor que cero"
    lista = []
    for numero in [i for i in range(1, N+1)]: 
        lista.append(numero**2)
    assert len(lista) == N
    return lista

def main():
    cuadrados = lista_cuadrados()
    print("\nUltimos 10 valores de la lista de cuadrados:")
    print(cuadrados[-10:])

if __name__ == "__main__":
    main()