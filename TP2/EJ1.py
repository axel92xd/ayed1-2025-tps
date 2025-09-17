import random as rn
from typing import List

def generar_lista_aleatoria() -> List[int]:
    """
    Genera una lista con números aleatorios de 4 dígitos.
    La cantidad de elementos es aleatoria, entre 10 y 99.

    Pre: ninguna
    Post: devuelve una lista de enteros entre 1000 y 9999.
    """
    cantidad = rn.randint(10, 99)
    lista = []
    for _ in [None]*cantidad:  
        lista.append(rn.randint(1000, 9999))
    assert all(1000 <= n <= 9999 for n in lista)
    return lista

def producto_total(lista: List[int]) -> int:
    """
    Calcula el producto de todos los elementos de una lista.

    Pre: lista no vacia
    Post: devuelve un entero positivo
    """
    assert lista, "La lista no puede estar vacia"
    resultado = 1
    for numero in lista:
        resultado *= numero
    assert resultado > 0
    return resultado

def eliminar_valor(lista: List[int], valor: int) -> List[int]:
    """
    Elimina todas las apariciones de un valor en la lista.

    Pre: lista de enteros y valor entero
    Post: la lista retornada no contiene el valor a eliminar
    """
    assert isinstance(valor, int)
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1
    assert valor not in lista
    return lista

def verificar_capicua(lista: List[int]) -> bool:
    """
    Determina si una lista es capicua.

    Pre: lista de enteros
    Post: True si es capicua, False en caso contrario
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True


def main():
    lista = generar_lista_aleatoria()
    print("Lista generada aleatoriamente:")
    print(lista)

    prod = producto_total(lista)
    print(f"\nProducto de todos los elementos: {prod}")

    valor_a_eliminar = int(input("\nIngrese un valor a eliminar de la lista: "))
    lista_modificada = eliminar_valor(lista[:], valor_a_eliminar)
    print("Lista despues de eliminar el valor:")
    print(lista_modificada)

    if verificar_capicua(lista):
        print("\nLa lista original es capicua.")
    else:
        print("\nLa lista original no es capicua.")

if __name__ == "__main__":
    main()
