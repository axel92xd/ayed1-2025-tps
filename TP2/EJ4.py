from typing import List

def eliminar_valores(lista: List[int], eliminar: List[int]) -> None:
    """
    Elimina de la lista original todos los elementos que estén en la lista de 'eliminar'.

    Pre: 'lista' y 'eliminar' deben ser listas de enteros.
    Post: 'lista' queda modificada, sin los valores que aparecen en 'eliminar'.
    """
    assert isinstance(lista, list) and isinstance(eliminar, list), "Deben ser listas"
    for valor in eliminar:
        while valor in lista:   # elimina todas las apariciones
            lista.remove(valor)

def main():
    lista_original = [10, 20, 30, 40, 20, 50, 30, 60]
    valores_a_eliminar = [20, 30, 70]

    print("Lista original:", lista_original)
    print("Valores a eliminar:", valores_a_eliminar)

    eliminar_valores(lista_original, valores_a_eliminar)

    print("Lista resultante:", lista_original)

if __name__ == "__main__":
    main()
