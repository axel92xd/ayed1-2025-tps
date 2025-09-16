import random as rn

def lista_aleatoria(n: int) -> list[int]:
    """
    Genera una lista de n números aleatorios entre 1 y 100.
    Pre: n es un entero positivo
    Post: devuelve una lista de n enteros aleatorios entre 1 y 100
    """
    assert n > 0, "n debe ser positivo"
    return [rn.randint(1, 100) for _ in range(n)]

def filtrar_impares(lista: list[int]) -> list[int]:
    """
    Devuelve una lista con los elementos impares de la lista original usando filter.
    Pre: lista es una lista de enteros
    Post: devuelve una lista de enteros impares
    """
    return list(filter(lambda x: x % 2 != 0, lista))

n = int(input("Ingrese la cantidad de números aleatorios: "))
lista = lista_aleatoria(n)
impares = filtrar_impares(lista)

print("Lista original:", lista)
print("Lista de impares:", impares)
