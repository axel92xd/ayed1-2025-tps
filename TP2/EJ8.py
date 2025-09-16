def impares_100_200() -> list[int]:
    """
    Construye una lista con todos los números impares entre 100 y 200.
    
    Pre: Ninguna
    Post: Devuelve una lista de enteros impares entre 100 y 200
    """
    lista_impares = [x for x in range(101, 201, 2)]  # empieza en 101, hasta 200
    assert all(x % 2 != 0 for x in lista_impares), "Todos deben ser impares"
    return lista_impares

impares_100_200()
