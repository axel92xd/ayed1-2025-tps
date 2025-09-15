import random as rn
from typing import List

# ==================== FUNCIONES ====================

def generar_lista_numeros() -> List[int]:
    """
    Genera una lista de N números aleatorios entre 1 y 100.
    N se ingresa por teclado.

    Pre: N > 0
    Post: Devuelve lista de enteros entre 1 y 100 de tamaño N
    """
    N = int(input("Ingrese la cantidad de números: "))
    assert N > 0, "N debe ser mayor que cero"

    lista = []
    contador = 0
    while contador < N:
        lista.append(rn.randint(1, 100))
        contador += 1

    assert len(lista) == N
    assert all(1 <= n <= 100 for n in lista)
    return lista

def tiene_elementos_repetidos(lista: List[int]) -> bool:
    """
    Determina si la lista tiene elementos repetidos.

    Pre: lista de enteros
    Post: True si hay repetidos, False si todos son únicos
    """
    assert isinstance(lista, list)
    for elemento in lista:
        if lista.count(elemento) > 1:
            return True
    return False

def obtener_elementos_unicos(lista: List[int]) -> List[int]:
    """
    Devuelve una lista con los elementos únicos de la lista original.

    Pre: lista de enteros
    Post: lista sin duplicados
    """
    assert isinstance(lista, list)
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    # Verificar que no hay duplicados en la nueva lista
    for e in unicos:
        assert unicos.count(e) == 1
    return unicos


def main():
    lista = generar_lista_numeros()
    print("\nLista generada:")
    print(lista)

    # Verificar si hay elementos repetidos
    print("\n¿Contiene elementos repetidos?:", tiene_elementos_repetidos(lista))

    # Lista con elementos únicos
    unicos = obtener_elementos_unicos(lista)
    print("\nLista con elementos únicos:")
    print(unicos)

# Ejecutar programa
if __name__ == "__main__":
    main()
