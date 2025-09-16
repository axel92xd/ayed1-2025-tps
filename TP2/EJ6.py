from typing import List

def normalizar_lista(valores: List[int]) -> List[float]:
    """
    Recibe una lista de enteros y devuelve una lista normalizada, 
    de manera que la suma de sus elementos sea 1.0, respetando las proporciones relativas.

    Pre: lista no vacía, elementos enteros >= 0
    Post: retorna lista de floats cuya suma es 1.0 si la lista no es toda cero,
          o lista de ceros si todos los elementos son 0.
    """

    assert isinstance(valores, list) and valores, "La lista no puede estar vacía"

    suma_total = sum(valores)
    lista_normalizada = []

    if suma_total == 0:
        for _ in valores:
            lista_normalizada.append(0.0)
    else:
        for valor in valores:
            lista_normalizada.append(valor / suma_total)

    return lista_normalizada


def main():
    lista1 = [1, 1, 2]
    lista2 = [5, 15, 10]
    lista3 = [3, 3, 3, 3]

    for lista in [lista1, lista2, lista3]:
        print(f"Lista Base: {lista} -> Normalizada: {normalizar_lista(lista)}")

    entrada = input("Ingrese números enteros separados por espacios: ")
    lista_usuario = [int(x) for x in entrada.split()]
    print("Lista normalizada:", normalizar_lista(lista_usuario))


if __name__ == "__main__":
    main()
