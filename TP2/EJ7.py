from typing import List

def intercalar_listas(lista1: List[int], lista2: List[int]) -> None:
    """
    Intercala los elementos de lista2 dentro de lista1 usando rebanadas.
    Modifica lista1 en el lugar.
    
    Pre: lista1 y lista2 son listas de enteros
    Post: lista1 queda modificada intercalando elementos de lista2
    """
    assert isinstance(lista1, list) and isinstance(lista2, list), "Ambas deben ser listas"

    min_len = min(len(lista1), len(lista2))
    
    for i in range(min_len):
        lista1[i*2+1:i*2+1] = [lista2[i]] 
    
    # Si lista2 es mas larga, agregar el resto al final de lista1
    if len(lista2) > len(lista1):
        lista1[len(lista1):len(lista1)] = lista2[min_len:]


def main():
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    print(f"Antes de intercalar:\nLista1: {lista1}\nLista2: {lista2}")
    
    intercalar_listas(lista1, lista2)
    
    print(f"Después de intercalar:\nLista1: {lista1}")


if __name__ == "__main__":
    main()
